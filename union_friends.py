from collections import defaultdict

if __name__ == "__main__":
    with open("target_users.txt") as file:
        users = [user.strip('\n') for user in file.readlines()]

    friends = defaultdict(list)
    for user in users:
        user_name = user.split('/')[-1]
        with open(f"{user_name}_friends.txt") as file:
            friends[user_name] = [friend.split(';')[0] for friend in file.readlines()]

    s1 = set(friends['vladimir.bugaevsky.1'])
    s2 = set(friends['e.pchelincev'])

    print(len(s1.intersection(s2)))



