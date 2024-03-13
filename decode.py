def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
        mapping = {int(line.split()[0]): line.split()[1] for line in lines}
        message = []
        count = 0
        for i in range(1, len(mapping) + 1):
            count += i
            if count in mapping:
                message.append(mapping[count])
        return ' '.join(message) if count == len(mapping) else False

print(decode('EncodedMessageList.txt'))

