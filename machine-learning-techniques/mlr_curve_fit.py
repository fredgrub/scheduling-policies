import numpy as np
import scipy.optimize as opt
from polynomials import *

SECONDS_IN_ONE_HOUR = 3600

def extract_score_distribution_with_parameters(filename):
    """
    Extract p, q, r and score from .csv file and return them as a numpy array.
    """

    p = []
    q = []
    r = []
    score = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.split(',')
            p.append(float(row[0]))
            q.append(float(row[1]))
            r.append(float(row[2]))
            score.append(float(row[3]))

    return np.array(p), np.array(q), np.array(r), np.array(score)

def fit_and_evaluate(f, p, q, r, score):
    """
    Use non-linear least squares to fit a function, f, to data. (p, q, r) are the parameters, and score is the data to 
    be fitted. The 1/p*q uncertainty emphasize that the fit must perform a good estimation of the score of large area
    jobs.
    
    Returns the optimized parameters and the estimated covariance matrix.
    """

    popt, pcov = opt.curve_fit(f, (p, q, r), score, sigma=(1.0/(p*q)), absolute_sigma=True)

    # Compute the mean absolute error of the fit.
    mae = np.mean(np.abs(f((p, q, r), *popt) - score))

    return popt, pcov, mae

def seconds_to_hours_normalization(list_of_numbers):
    """
    Convert a list of numbers in seconds to hours.
    """

    return np.array(list(map(lambda x: x / SECONDS_IN_ONE_HOUR, list_of_numbers)))

def normalize_temporal_variables(runtimes, submittals):
    """
    Normalize temporal variables using the seconds-to-hours normalization.
    """

    return seconds_to_hours_normalization(runtimes), seconds_to_hours_normalization(submittals)

def main():
    # get the distribution variables
    filename = "score-distribution-1.csv"
    p, q, r, score = extract_score_distribution_with_parameters(filename)
    
    # apply temporal normalization
    p, r = normalize_temporal_variables(p, r)

    functions = [lin, qdr, cub, qua, qui, sex]
    functions_labels = ["lin", "qdr", "cub", "qua", "qui", "sex"]

    for i, polynomial in enumerate(functions):
        # fit and evaluate the model with polynomial
        popt, _, mae = fit_and_evaluate(polynomial, p, q, r, score)
        
        print(f"*** {functions_labels[i]}")
        print(f"MAE = {mae:e}")
        
        # save the optimized parameters to a file named as the polynomial name
        np.savetxt(f"Parameters/{functions_labels[i]}_normalized.txt", popt)

if __name__ == '__main__':
    main()