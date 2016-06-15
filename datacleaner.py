#!/usr/bin/env python3

'''1.Listwise Deletion
    Delete all data from any participant with missing values.
    If your sample is large enough, then you likely can drop data without substantial loss of statistical power.
    Be sure that the values are missing at random and that you are not inadvertently removing a class of participants'''

'''2.Recover the Values
    You can sometimes contact the participants and ask them to fill out the missing values.
    For in-person studies, we've found having an additional check for missing values before the participant leaves helps.'''

'''3.Educated Guessing:
    It sounds arbitrary and isn't your preferred course of action, but you can often infer a missing value.
    For related questions, for example, like those often presented in a matrix,
    if the participant responds with all "4s", assume that the missing value is a 4.'''

'''4.Average Imputation:
    Use the average value of the responses from the other participants to fill in the missing value.
    If the average of the 30 responses on the question is a 4.1, use a 4.1 as the imputed value.
    This choice is not always recommended because it can artificially reduce the variability of your data but in some cases makes sense.'''

'''5.Common-Point Imputation:
    For a rating scale, using the middle point or most commonly chosen value.
    For example, on a five-point scale, substitute a 3, the midpoint, or a 4, the most common value (in many cases).
    This is a bit more structured than guessing, but it's still among the more risky options.
    Use caution unless you have good reason and data to support using the substitute value.'''

'''6.Regression Substitution:
    You can use multiple-regression analysis to estimate a missing value.
    We use this technique to deal with missing SUS scores. Regression substitution predicts the missing value from the other values.'''
    
'''7.Multiple Imputation:
    The most sophisticated and, currently, most popular approach is to take the regression idea further and take advantage of
    correlations between responses. In multiple imputation [pdf], software creates plausible values based on the correlations for
    the missing data and then averages the simulated datasets by incorporating random errors in your predictions. It is one of a number of examples
    where computers continue to change the statistical landscape. Most statistical packages like SPSS come with a multiple-imputation feature.
    More on multiple imputation.'''
    

def ListwiseDeletion(df):
    for column in df.columns:
        print(column)
    
    