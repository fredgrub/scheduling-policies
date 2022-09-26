#include <math.h>
#include "polynomials.h"

double linear(double p, double q, double r)
{
    // Obtained from score-distribution-1.csv
    double t0 = 3.166889358468361060e-02;
    double t1 = 1.242149158119801963e-07;
    double t2 = 3.102223098109877219e-05;
    double t3 = -1.627303114515290627e-07;
    
    return t0 + t1*p + t2*q + t3*r;
}

double quadratic(double p, double q, double r)
{
    // Obtained from score-distribution-1.csv
    double t0 = 3.590707241156540497e-02;
    double t1 = 3.576538144567375239e-07;
    double t2 = -3.053216185525264864e-05;
    double t3 = -4.328087997453563895e-07;
    double t4 = -3.685981376853831304e-12;
    double t5 = 1.463611569955363050e-07;
    double t6 = 2.949993262407820555e-12;
    double t7 = 4.791070470023183499e-10;

    
    return t0 + t1*p + t2*q + t3*r \
            + t4*pow(p,2) + t5*pow(q,2) + t6*pow(r,2) \
            + t7*p*q;
}

double cubic(double p, double q, double r)
{
    // Obtained from score-distribution-1.csv
    double t0 = 4.674193719461900570e-02;
    double t1 = -4.818059660453959125e-07;
    double t2 = -1.153044575165454341e-04;
    double t3 = -7.876109690791398410e-07;
    double t4 = 1.534668007720631469e-11;
    double t5 = 5.389352103056937363e-07;
    double t6 = 1.093272703798870775e-11;
    double t7 = 6.225969817731758866e-09;
    double t8 = -8.637182634068220160e-17;
    double t9 = -1.119522920768794542e-09;
    double t10 = -4.024373112904794642e-17;
    double t11 = -9.864975966001858903e-14;
    double t12 = -1.268174792590604567e-12;

    
    return t0 + t1*p + t2*q + t3*r \
            + t4*pow(p,2) + t5*pow(q,2) + t6*pow(r,2) \
            + t7*p*q \
            + t8*pow(p,3) + t9*pow(q,3) + t10*pow(r,3) \
            + t11*pow(p,2)*q + t12*p*pow(q,2);
}

double quartic(double p, double q, double r)
{
    // Obtained from score-distribution-1.csv
    double t0 = 4.728300407411587664e-02;
    double t1 = -9.609424200010661146e-07;
    double t2 = -3.287178989157210380e-05;
    double t3 = -6.454563093015281803e-07;
    double t4 = 4.396132186296871353e-11;
    double t5 = 5.470006004565999598e-07;
    double t6 = 5.341610299878868999e-12;
    double t7 = -3.199572132883175374e-10;
    double t8 = -6.130312409653983099e-16;
    double t9 = -6.445611168080488591e-09;
    double t10 = 2.881219165320355338e-17;
    double t11 = -1.008940620408811455e-14;
    double t12 = 3.944348188382883082e-11;
    double t13 = 2.637143896092424608e-21;
    double t14 = 1.745778474429483138e-11;
    double t15 = -2.536596914374795946e-22;
    double t16 = -3.649649805587642395e-19;
    double t17 = -1.175093431992154723e-16;
    double t18 = -9.710179614628395804e-14;

    
    return t0 + t1*p + t2*q + t3*r \
            + t4*pow(p,2) + t5*pow(q,2) + t6*pow(r,2) \
            + t7*p*q \
            + t8*pow(p,3) + t9*pow(q,3) + t10*pow(r,3) \
            + t11*pow(p,2)*q + t12*p*pow(q,2) \
            + t13*pow(p,4) + t14*pow(q,4) + t15*pow(r,4) \
            + t16*pow(p,3)*q + t17*pow(p,2)*pow(q,2) + t18*p*pow(q,3);
}

double quintic(double p, double q, double r)
{
    // Obtained from score-distribution-1.csv
    double t0 = 1.901793665277802872e-02;
    double t1 = 6.175943371192469091e-06;
    double t2 = -1.981593681574161448e-04;
    double t3 = -8.543828331877053710e-07;
    double t4 = -4.430633337162827286e-10;
    double t5 = 5.446882062706825955e-06;
    double t6 = 1.846080456387081807e-11;
    double t7 = -2.672336512733551946e-08;
    double t8 = 1.224313381476174815e-14;
    double t9 = -2.771415166795075111e-08;
    double t10 = -2.617357096217345128e-16;
    double t11 = 2.843682378335922489e-12;
    double t12 = -2.104694588591718568e-10;
    double t13 = -1.336503033896480125e-19;
    double t14 = 5.474118968629603573e-11;
    double t15 = 2.262120606921343941e-21;
    double t16 = -7.130293214085002955e-17;
    double t17 = 1.570614920661742082e-15;
    double t18 = 7.799468528214064637e-13;
    double t19 = 4.842450682189720520e-25;
    double t20 = -4.160351715876901583e-14;
    double t21 = -7.336412798911820543e-27;
    double t22 = 4.268627189936061731e-22;
    double t23 = 6.576310199422058470e-20;
    double t24 = -1.613895255677063337e-17;
    double t25 = -4.751092431858810739e-17;


    return t0 + t1*p + t2*q + t3*r \
            + t4*pow(p,2) + t5*pow(q,2) + t6*pow(r,2) \
            + t7*p*q \
            + t8*pow(p,3) + t9*pow(q,3) + t10*pow(r,3) \
            + t11*pow(p,2)*q + t12*p*pow(q,2) \
            + t13*pow(p,4) + t14*pow(q,4) + t15*pow(r,4) \
            + t16*pow(p,3)*q + t17*pow(p,2)*pow(q,2) + t18*p*pow(q,3) \
            + t19*pow(p,5) + t20*pow(q,5) + t21*pow(r,5) \
            + t22*pow(p,4)*q + t23*pow(p,3)*pow(q,2) \
            + t24*pow(p,2)*pow(q,3) + t25*p*pow(q,4);
}

double sextic(double p, double q, double r)
{
    // Obtained from score-distribution-1.csv
    double t0 = 7.627245316569174205e-02;
    double t1 = -1.117556042438734965e-05;
    double t2 = 2.372235782652555060e-04;
    double t3 = -9.932770913173939328e-07;
    double t4 = 9.213120153927131747e-10;
    double t5 = -2.897447118911207828e-05;
    double t6 = 2.483241474694971285e-11;
    double t7 = 2.048039233631151074e-07;
    double t8 = -3.139850543226848936e-14;
    double t9 = 3.388454922870230954e-07;
    double t10 = -3.547539350328793551e-16;
    double t11 = -1.849430426152291401e-11;
    double t12 = 1.979396889813338279e-10;
    double t13 = 5.028319487613075303e-19;
    double t14 = -1.700928500778174479e-09;
    double t15 = 2.632359402887012865e-21;
    double t16 = 5.564458826197205399e-16;
    double t17 = 5.743195450203889573e-14;
    double t18 = -8.791280347368572346e-12;
    double t19 = -3.732976593631910452e-24;
    double t20 = 4.119640014146281281e-12;
    double t21 = -6.462831980477734338e-27;
    double t22 = -6.610385628987309580e-21;
    double t23 = -1.631386537751762037e-18;
    double t24 = 2.670764785483803400e-17;
    double t25 = 3.040027246761647098e-14;
    double t26 = 1.026817781627861999e-29;
    double t27 = -3.929111267920459539e-15;
    double t28 = -5.525711662209033766e-33;
    double t29 = 2.623820144373433037e-26;
    double t30 = 1.140746177481603963e-23;
    double t31 = 8.600856317356497864e-22;
    double t32 = -1.613397120222877604e-19;
    double t33 = -3.222835453728692674e-17;



    return t0 + t1*p + t2*q + t3*r \
            + t4*pow(p,2) + t5*pow(q,2) + t6*pow(r,2) \
            + t7*p*q \
            + t8*pow(p,3) + t9*pow(q,3) + t10*pow(r,3) \
            + t11*pow(p,2)*q + t12*p*pow(q,2) \
            + t13*pow(p,4) + t14*pow(q,4) + t15*pow(r,4) \
            + t16*pow(p,3)*q + t17*pow(p,2)*pow(q,2) + t18*p*pow(q,3) \
            + t19*pow(p,5) + t20*pow(q,5) + t21*pow(r,5) \
            + t22*pow(p,4)*q + t23*pow(p,3)*pow(q,2) \
            + t24*pow(p,2)*pow(q,3) + t25*p*pow(q,4) \
            + t26*pow(p,6) + t27*pow(q,6) + t28*pow(r,6) \
            + t29*pow(p,5)*q + t30*pow(p,4)*pow(q,2) \
            + t31*pow(p,3)*pow(q,3) \
            + t32*pow(p,2)*pow(q,4) + t33*p*pow(q,5);
}