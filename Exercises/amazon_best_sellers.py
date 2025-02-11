import numpy as np

def load_dataset(filename):
    # Load the CSV to a NumPy array with named columns
    dataset = np.genfromtxt(filename, delimiter=';', dtype=None, names=True, encoding='utf-8')
    return dataset

def mean_score(dataset):
    # Calculate the mean User Rating of the best selling books
    return round(np.mean(dataset['User_Rating']), 15)

def mean_price(dataset, genre):
    # Calculate the mean Price of books of a given genre
    genre_mask = dataset['Genre'] == genre
    return round(np.mean(dataset['Price'][genre_mask]), 15)

def best_selling_authors(dataset):
    # Generate the top 15 best selling authors for 2009 to 2019
    authors, counts = np.unique(dataset['Author'], return_counts=True)
    sorted_indices = np.argsort(counts)[::-1]
    
    top_authors = {}
    for i in range(15):
        author = authors[sorted_indices[i]]
        count = counts[sorted_indices[i]]
        top_authors[author] = count
    
    return top_authors

if __name__ == "__main__":
    dataset = load_dataset('bestsellers.csv')

    mean_user_rating = mean_score(dataset)
    mean_fiction_price = mean_price(dataset, 'Fiction')
    
    print(mean_user_rating)
    print(mean_fiction_price)
    
    print("\n")
    
    top_authors = best_selling_authors(dataset)
    for author, count in top_authors.items():
        print(f"{author}: {count}")
