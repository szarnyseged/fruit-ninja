import mysql.connector


"""
db name: fruit ninja
table name: highscores (id, name, score)
"""

try:
    fruit_ninja_db=mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor=fruit_ninja_db.cursor()

except mysql.connector.Error as err:
    pass



def upload_score(name, score):
    cursor.execute("USE fruit_ninja;")
    sql= "INSERT INTO highscores (name, score) VALUES ( %s, %s);"
    val= (name, score)
    cursor.execute(sql, val)
    fruit_ninja_db.commit()



    

