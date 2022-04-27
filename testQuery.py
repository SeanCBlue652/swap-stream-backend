import dao

def testAddUser():
    for n in range(17,40):
        dao.add_user(n, "'{Stone}'", "'{Spotify}'")

testAddUser()
print(dao.get_test_data())