from chapter2.vec import Vec
from chapter2.vecutil import zero_vec
from sys import maxsize
import operator as op

# 2.12.1
def create_voting_dict(strlist):
    """
    :param strlist: strlist: list of strings representing voting records. Each line space delimited {last_name} {party} {state} {votes...}
    :return: Dictionary mapping last name to list of integer votes: -1, 0, 1 (no, abstain, yes)

    >>> strlist = ['Lesko D MD 1 0 -1 0 1', 'Klein R MA 0 1 1 -1 0']
    >>> voting_dict = create_voting_dict(strlist)
    >>> voting_dict['Lesko'][2] == -1
    True
    >>> voting_dict['Klein'][4] == 0
    True
    """
    voting_dict = dict()
    for line in strlist:
        elements = line.split(' ')
        voting_dict[elements[0]] = [int(e) for e in elements[3:]]
    return voting_dict


# 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Compre records of two senators
    :param sen_a: senator last name
    :param sen_b: other senator last name
    :param voting_dict: dictionary of voting record by last name
    :return: dot-product representing degree of similarity between two senators' voting policies

    >>> strlist = ['Lesko D MD 1 0 -1 0 1', 'Klein R MA 0 1 1 -1 0']
    >>> voting_dict = create_voting_dict(strlist)
    >>> policy_compare('Lesko', 'Klein', voting_dict)
    -1
    """
    sen_a_votes = voting_dict[sen_a]
    sen_b_votes = voting_dict[sen_b]
    sen_a_vec = votes2vec(sen_a_votes)
    sen_b_vec = votes2vec(sen_b_votes)
    return sen_a_vec * sen_b_vec

def votes2vec(votes):
    """
    Convert list of votes to vector. Labels are ordinal position.
    :param votes: list of numeric votes
    :return: vector representing list of votes
    """
    return Vec(set(range(len(votes))), {i: v for i, v in enumerate(votes)})


# 2.12.3
def specifier_similar(sen, voting_dict, specifier):
    """
    Find senator with voting record based on specifier passed, excluding the senator passed
    :param sen: senator last name
    :param voting_dict: dictionary of voting record by last name
    :param specifier: > or < (greater than - "most" - or less than - "least"
    :return: senator last name with most similar record, in case of a tie chooses first alphabetically
    """
    specifier_lookup = {'<': op.lt, '>': op.gt}
    similar = {'score': (1 if specifier_lookup[specifier] == op.lt else -1) * maxsize, 'sen': None}

    sen_vec = votes2vec(voting_dict[sen])

    for other_sen in sorted(voting_dict.keys()):
        if other_sen == sen: continue
        if similar['sen'] is None: similar['sen'] = other_sen
        other_sen_vec = votes2vec(voting_dict[other_sen])
        similarity = other_sen_vec * sen_vec
        # print(similarity, other_sen, similar_score, similar_sen, specifier_lookup[specifier](similarity, similar_score))
        if specifier_lookup[specifier](similarity, similar['score']):
            similar = {'score': similarity, 'sen': other_sen}
    # print(similar_score)
    return similar


def most_similar(sen, voting_dict):
    """
    Find senator with voting record most similar, excluding the senator passed
    :param sen: senator last name
    :param voting_dict: dictionary of voting record by last name
    :return: senator last name with most similar record, in case of a tie chooses first alphabetically

    >>> voting_dict = create_voting_dict(list(open('voting_record_dump109.txt')))
    >>> most_similar('Mikulski', voting_dict)
    'Biden'
     >>> most_similar('Chafee', voting_dict) # 2.12.5
     'Jeffords'
    """
    return specifier_similar(sen, voting_dict, '>')['sen']

# 2.12.4
def least_similar(sen, voting_dict):
    """
    Find senator with voting record least similar, excluding the senator passed
    :param sen: senator last name
    :param voting_dict: dictionary of voting record by last name
    :return: senator last name with least similar record, in case of a tie chooses first alphabetically

    >>> voting_dict = create_voting_dict(list(open('voting_record_dump109.txt')))
    >>> least_similar('Mikulski', voting_dict)
    'Inhofe'
    >>> least_similar('Santorum', voting_dict) # 2.12.5
    'Feingold'
    """
    return specifier_similar(sen, voting_dict, '<')['sen']

# 2.12.7
def find_average_similarity(sen, sen_set, voting_dict):
    """
    :param sen: senator last name to compare against others
    :param sen_set: list of other senator last names to compare against
    :param voting_dict: dictionary of voting record by last name
    :return: average dot product for all senators compared to

    >>> strlist = list(open('voting_record_dump109.txt'))
    >>> sen_set = [line.split(' ')[0] for line in strlist if line.split(' ')[1] == 'D']
    >>> voting_dict = create_voting_dict(strlist)
    >>> average_similarities = {sen:find_average_similarity(sen, sen_set, voting_dict) for sen in sen_set}
    >>> sort_dict_by_value(average_similarities)[0][0]
    'Biden'
    """
    sen_vec = votes2vec(voting_dict[sen])
    similarity_score = 0
    for other_sen in sen_set:
        if other_sen == sen: continue # skip passed senator
        other_sen_vec = votes2vec(voting_dict[other_sen])
        similarity_score += sen_vec * other_sen_vec

    return similarity_score / (len(sen_set) - 1)

def sort_dict_by_value(d, reverse=True):
    return [(k, d[k]) for k in sorted(d, key=d.get, reverse=reverse)]

# 2.12.8
def find_average_record(sen_set, voting_dict):
    """
    Find the average voting record
    :param sen_set: set of last names
    :param voting_dict: dictionary of voting record by last name
    :return: average voting record vector

    >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
    >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
    Vec({0, 1, 2},{0: -0.5, 1: -0.5, 2: 0.0})
    >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
    >>> find_average_record({'a','c','e'}, d)
    Vec({0, 1, 2},{0: -0.6666666666666666, 1: -0.3333333333333333, 2: 0.6666666666666666})
    >>> find_average_record({'a','c','e','b'}, d)
    Vec({0, 1, 2},{0: -0.5, 1: 0.0, 2: 0.75})
    >>> find_average_record({'a'}, d)
    Vec({0, 1, 2},{0: 0.0, 1: 1.0, 2: 1.0})

    >>> strlist = list(open('voting_record_dump109.txt'))
    >>> sen_set = [line.split(' ')[0] for line in strlist if line.split(' ')[1] == 'D']
    >>> voting_dict = create_voting_dict(strlist)
    >>> average_Democrat_record = find_average_record(sen_set, voting_dict)
    >>> similarity_to_average_Democrat_record = {sen:average_Democrat_record*votes2vec(voting_dict[sen]) for sen in sen_set}
    >>> sort_dict_by_value(similarity_to_average_Democrat_record)[0][0]
    'Biden'
    """
    sum_vec = None
    for sen in sen_set:
        sen_vec = votes2vec(voting_dict[sen])
        if sum_vec is None: sum_vec = zero_vec(sen_vec.D)
        sum_vec += sen_vec

    return sum_vec / len(sen_set)

# 2.12.9
def bitter_rivals(voting_dict):
    """
    Find the two senators with the largest disagreement
    :param voting_dict: dictionary of voting record by last name
    :return: 2-tuple of senators who disagree the most

    >>> voting_dict = create_voting_dict(list(open('voting_record_dump109.txt')))
    >>> sort_dict_by_value(bitter_rivals(voting_dict), False)[0][0]
    ('Feingold', 'Inhofe')
    """
    similarity = dict()
    for sen in voting_dict.keys():
        least = specifier_similar(sen, voting_dict, '<')
        similarity[tuple(sorted([least['sen'], sen]))] = least['score']

    return similarity