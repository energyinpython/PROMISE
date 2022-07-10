import numpy as np
from pyrepo.mcda_methods import PROMETHEE_II
from pyrepo import normalizations as norms
from pyrepo.additions import rank_preferences

def main():

    # provide decision matrix in array numpy.darray
    matrix = np.array([[8, 7, 2, 1],
    [5, 3, 7, 5],
    [7, 5, 6, 4],
    [9, 9, 7, 3],
    [11, 10, 3, 7],
    [6, 9, 5, 4]])

    # provide criteria weights in array numpy.darray. All weights must sum to 1.
    weights = np.array([0.4, 0.3, 0.1, 0.2])

    # provide criteria types in array numpy.darray. Profit criteria are represented by 1, and cost criteria by -1.
    types = np.array([1, 1, 1, 1])

    # provide p or q or both p and q parameters depending on chosen preference function
    p = 2 * np.ones(len(weights))
    q = 1 * np.ones(len(weights))

    # Create the PROMETHEE II method object. PROMETHEE II does not require normalization method.
    promethee_II = PROMETHEE_II()

    # provide preference functions selected from six preference functions available for PROMETHEE II for each criterion
    preference_functions = [promethee_II._level_function for pf in range(len(weights))]

    # Calculate the PROMETHEE II preference values of alternatives
    pref = promethee_II(matrix, weights, types, preference_functions = preference_functions, p = p, q = q)

    # Generate ranking of alternatives by sorting alternatives descendingly according to the PROMETHEE II algorithm (reverse = True means sorting in descending order) according to preference values
    rank = rank_preferences(pref, reverse=True)

    print('Preference values: ', np.round(pref, 4))
    print('Ranking: ', rank)


if __name__ == '__main__':
    main()