from collections import defaultdict

if __name__ == "__main__":
    with open("target_users.txt") as file:
        users = [user.strip('\n') for user in file.readlines()]

    friends = defaultdict(list)
    for user in users:
        user_name = user.split('/')[-1]
        with open(f"{user_name}_friends.txt") as file:
            friends[user_name] = [friend.split(';')[0] for friend in file.readlines()]

    with open("users.txt") as file:
        parsed_users = [line for line in file.readlines()]

    for user_name, friends_links in friends.items():
        with open(f"{user_name}.txt", "w") as file:
            for item in parsed_users:
                friend_info = item.strip('\n').split(';')
                if friend_info[0] in friends_links:

                    file.write(f"{friend_info[0]};{';'.join(friend_info[1:3])}\n")





