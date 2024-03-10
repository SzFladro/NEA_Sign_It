import sqlite3

'''
    Connects to the database and inserts data (word_name, download_link, category_id) into the Words table

    Parameters:
        data_array (list): list of tuples containing word data in the format (word_name, download_link)
        category_id (int): Category ID to associate with the inserted words

'''
def insert_words_data(data_array, category_id):

    conn = sqlite3.connect("SIGNIT2.db")
    cursor = conn.cursor()
    for index, (word_name, download_link) in enumerate(data_array, start=1):
        cursor.execute(
            "INSERT INTO Words (word_name, download_link, Cat_ID) VALUES (?, ?, ?)",
            (word_name, download_link, category_id)
        )
        print(f"Inserted data for Word {index}: {word_name}")
    conn.commit()
    conn.close()

data_array = [
    ("A", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/A%20-over.mp4?alt=media&token=f0ecc4fd-e71b-42f0-bbf7-7de4c6343ed1"),
    ("B", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/B%20-over.mp4?alt=media&token=3267ea49-278b-4000-8ec3-6a098127e25a"),
    ("C", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/C%20-over.mp4?alt=media&token=4c0ef7f1-8761-484b-8545-d702c551fd36"),
    ("D", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/D%20-over.mp4?alt=media&token=8dd7397d-6472-4e2f-929e-ed72bc990fd7"),
    ("E", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/E%20-over.mp4?alt=media&token=00d07a02-13ed-48e3-9c9c-1c4fb6ce1488"),
    ("F", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/F%20-over.mp4?alt=media&token=006a4268-c655-49e4-8572-44751dce065e"),
    ("G", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/G%20-over.mp4?alt=media&token=6f64bdb3-77f0-442c-b653-d032bd108871"),
    ("H", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/H%20-over.mp4?alt=media&token=1cdd66b1-3287-4b27-9aab-0c6e2a1bf283"),
    ("I", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/I%20-over.mp4?alt=media&token=a11984a5-e13d-4e4c-9a59-e208d788d4e7"),
    ("J", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/J%20-over.mp4?alt=media&token=2d208c71-cca0-4fdc-bfa0-c76acbf91f82"),
    ("K", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/K%20-over.mp4?alt=media&token=c2b19639-5c5b-4c3d-aa6b-b4746a919beb"),
    ("L", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/L%20-over.mp4?alt=media&token=efdceea2-c2f0-4236-b282-324602c615e8"),
    ("M", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/M%20-over.mp4?alt=media&token=d58bd11e-f0d2-41a7-806f-5574deb23482"),
    ("N", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/N%20-over.mp4?alt=media&token=6697ec06-7d75-43b5-a52a-b6b0cbd212f2"),
    ("O", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/O%20-over.mp4?alt=media&token=b901e3aa-3cf1-4f9e-9482-6470594538e5"),
    ("P", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/P%20-over.mp4?alt=media&token=32fe02c0-00c5-438e-8de0-f1f45c0eecfd"),
    ("Q", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/Q%20-over.mp4?alt=media&token=d02aab40-84ac-49a7-96bd-e2bca3501b80"),
    ("R", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/R%20-over.mp4?alt=media&token=1097c06a-ed60-49bd-a636-f89767479dd3"),
    ("S", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/S%20-over.mp4?alt=media&token=39494fbe-fb2c-4a04-bf6c-8d72980bd77f"),
    ("T", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/T%20over.mp4?alt=media&token=f7cc6668-dee4-4fa2-b6e6-1e5d5e7bdd2a"),
    ("U", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/U%20-over.mp4?alt=media&token=60bd9ea3-1860-4cf3-a5d5-b2189dca68ab"),
    ("V", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/V%20-over.mp4?alt=media&token=9c0c3646-58c0-4ffd-bf78-215e58f44de3"),
    ("W", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/W%20-over.mp4?alt=media&token=ce8ef0e4-c0b7-4ec6-90b3-ce15fc06ea74"),
    ("X", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/X%20-over.mp4?alt=media&token=77f5aa6a-e9b1-42c1-8f9f-02cecde27e2c"),
    ("Y", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/Y%20-over.mp4?alt=media&token=75a15070-2f53-4edb-b90b-45945a6622e8"),
    ("Z", "https://firebasestorage.googleapis.com/v0/b/sign-it-1.appspot.com/o/Z%20-over.mp4?alt=media&token=9383c558-677d-41b3-a8cd-e3ab371b97c2")
]

insert_words_data(data_array, category_id=1)
