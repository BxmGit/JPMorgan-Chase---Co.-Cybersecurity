import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv("transactions.csv")

def exercise_0(file):
    pass
#Return the column names as a list from the dataframe. 
def exercise_1(df):
    column_names = df.columns.tolist()
    return column_names

#Return the first k rows from the database
def exercise_2(df, k):
    first_k_rows = df.head(k)
    return(first_k_rows)

#Return a random sample of unique transaction types.  
def exercise_3(df, k):
    random_rows = df.sample(n=k)
    return random_rows
#Return a list of the unique transaction types.
def exercise_4(df):
    transaction_types = df['type'].unique().tolist()
    return transaction_types

#Return a Pandas series of the top 10 transaction destinations with frequencies.
def exercise_5(df):
    top_destinations = df['nameDest'].value_counts().head(10)
    return top_destinations

#Return all the rows from the dataframe for which fraud was detected.
def exercise_6(df):
    fraud_detected = df[df['isFraud'] == 1]
    return fraud_detected

#Bonus. Return a dataframe that contains the number of distinct destinations that each source has interacted with to, sorted in descending order.
def exercise_7(df):
    result = df.groupby('nameOrig').agg(
    distinct_destinations=pd.NamedAgg(column='nameDest', aggfunc='nunique'))
    result_sorted = result.sort_values(by='distinct_destinations', ascending=False)
    return result_sorted

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()
        
    def transaction_counts_split_by_fraud(df):
        return pd.crosstab(df['type'], df['isFraud'])
        

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Distribution of Transaction Types')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Frequncy of Transactions')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Type Split By Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Frequency')
    fig.suptitle('Analysis of Transaction Types')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return "The first chart provides a distribution of different transaction types, helping to identify which types are most common. The second chart breaks down these transaction types by fraud status, offering insights into which types of transactions are more prone to fraud."


def visual_2(df):
    def query(df):
        cash_out_df = df[df['type'] == 'CASH_OUT'].copy()

        # Calculate balance deltas for origin and destination accounts
        cash_out_df['orig_balance_delta'] = cash_out_df['newbalanceOrig'] - cash_out_df['oldbalanceOrg']
        cash_out_df['dest_balance_delta'] = cash_out_df['newbalanceDest'] - cash_out_df['oldbalanceDest']
        return cash_out_df
    
    plot = query(df).plot.scatter(x='orig_balance_delta',y='dest_balance_delta')
    plot.set_title('Origin vs Destination Account Balance Delta for Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return "This scatter plot visualizes the relationship between the changes in balance for origin and destination accounts specifically for 'CASH_OUT' transactions. Points above the x-axis represent transactions where the destination account’s balance increased, while points to the right of the y-axis represent transactions where the origin account’s balance decreased."


def exercise_custom(df):
        # Calculate the IQR of the 'amount'
        Q1 = df['amount'].quantile(0.25)
        Q3 = df['amount'].quantile(0.75)
        IQR = Q3 - Q1

        # Define outliers as any points outside of Q1 - 1.5*IQR and Q3 + 1.5*IQR
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filter out the outliers
        filtered_df = df[(df['amount'] > lower_bound) & (df['amount'] < upper_bound)]
        
        return filtered_df[['amount', 'isFraud']]
    
def visual_custom(df):
    data = exercise_custom(df)
    
    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plot = sns.scatterplot(data=data, x='amount', y='isFraud', alpha=0.5)
    
    plot.set_title('Transaction Amount vs Fraud Status')
    plot.set_xlabel('Transaction Amount')
    plot.set_ylabel('Fraud Status')
    plot.set_yticks([0, 1])
    plot.set_yticklabels(['Not Fraud', 'Fraud'])
    
    plt.show()
    
    return "This scatter plot, shows the relationship between transaction amount getting larger and fraud status. It provides a clear view on the common sizes of transaction which relate to fraud, helping to identify patterns or trends."
