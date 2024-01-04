import sqlite3

# Function to select data from 'words' and 'Categories' tables
def select_words_data(category_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("SIGNIT2.db")
    cursor = conn.cursor()

    # Select download links and categories from 'words' table with Cat_ID = 1
    cursor.execute("""
        SELECT Words.word_name, Words.download_link, Categories.Cat_name
        FROM Words
        JOIN Categories ON Words.Cat_ID = Categories.Cat_ID
        WHERE Words.Cat_ID = ?
    """, (category_id,))

    # Fetch all the selected rows
    rows = cursor.fetchall()

    # Display the result
    for row in rows:
        print("Word Name:", row[0])
        print("Download Link:", row[1])
        print("Category:", row[2])
        print("-----------")

    # Close the connection
    conn.close()

# Call the function to select data
select_words_data(category_id=1)
