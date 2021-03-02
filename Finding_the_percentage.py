# Finding the percentage

from statistics import mean

if __name__ == '__main__':
    records = {
        'alpha': [20, 30, 40],
        'beta': [30, 50, 70]
    }
    print(mean(records.get('beta')))
