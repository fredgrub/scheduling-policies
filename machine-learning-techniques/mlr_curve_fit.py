import numpy as np
import scipy.optimize as opt
from polynomials import *

# Extract p, q, r and score from csv file and return it as a numpy array.
def extract_data_from_csv(filename):
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

def fit_and_eval(func, p, q, r, score):
    # Run opt.curve_fit() using func as the model function, (p, q, r) as the parameters, score as the data to be fitted and
    # let sigma be 1.0/(p*q) with absolute_sigma=true. Return the optimized parameters and covariance matrix.
    popt, pcov = opt.curve_fit(func, (p, q, r), score, sigma=(1.0/(p*q)), absolute_sigma=True)

    # Compute the mean absolute error of the fit.
    mae = np.mean(np.abs(func((p, q, r), *popt) - score))

    return popt, pcov, mae


def main():
    # extract p, q, r and score from csv file and return it as a numpy array
    p, q, r, score = extract_data_from_csv("score-distribution-1.csv")
    
    functions = [lin, sqr, cub, qua, qui, sex]
    functions_labels = ["Lin", "Sqr", "Cub", "Qua", "Qui", "Sex"]

    for i, polynomial in enumerate(functions):
        # fit and evaluate the model with polynomial
        popt, _, mae = fit_and_eval(polynomial, p, q, r, score)
        
        print(f"*** {functions_labels[i]}")
        print(f"MAE = {mae:e}")
        
        # save the optimized parameters to a file named as the polynomial name
        np.savetxt(f"Parameters/{functions_labels[i]}_parameters.txt", popt)

if __name__ == '__main__':
    main()