import pandas as pd
import scipy.sparse as sparse
from implicit.als import AlternatingLeastSquares

# Function to create user-item matrix
def create_user_item_matrix(events):
    # Data preprocessing
    events = events.dropna(subset=['event'])  # Drop rows with missing 'event'
    events['event'] = events['event'].replace({'view': 1.0, 'addtocart': 2.0, 'transaction': 3.0})  # Convert event types
    
    # Group events by user and item, aggregate if necessary
    user_item_interaction = events.groupby(['visitorid', 'itemid'])['event'].sum().reset_index()

    # Assign unique IDs to users and items
    user_item_interaction['visitorid'] = user_item_interaction['visitorid'].astype("category")
    user_item_interaction['itemid'] = user_item_interaction['itemid'].astype("category")
    
    # Create a sparse matrix of all the user/item/event triples
    sparse_data = sparse.coo_matrix((user_item_interaction['event'].astype(float),
                                     (user_item_interaction['visitorid'].cat.codes.copy(),
                                      user_item_interaction['itemid'].cat.codes.copy())))
    
    # Convert to CSR format for efficiency
    user_item_matrix = sparse_data.tocsr()
    
    # Return matrix and lists of unique userids and itemids
    return user_item_matrix, user_item_interaction['visitorid'].cat.codes.copy().unique(), user_item_interaction['itemid'].cat.codes.copy().unique()

def main():
    # Load your events data from CSV
    events = pd.read_csv('/kaggle/input/ecommerce-dataset/events.csv')

    # Create user-item matrix and get userids and itemids
    user_item_matrix, userids, itemids = create_user_item_matrix(events)

    # Initialize ALS model
    als_model = AlternatingLeastSquares(factors=15, regularization=0.1, iterations=50)

    # Fit the model
    als_model.fit(user_item_matrix)

    # Get top-N recommendations for a user (e.g., user with ID 124)
    recommendations = als_model.recommend(124, sparse_user_items[124])
    print(recommendations)

if __name__ == "__main__":
    main()
