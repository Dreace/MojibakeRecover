from encodings.aliases import aliases

encoding_list = list(set(aliases.values()))


def main():
    src_text = input("需要恢复的字符串：")
    for item_i in encoding_list:
        for item_j in encoding_list:
            try:
                guess_text = src_text.encode(encoding=item_i).decode(encoding=item_j)
                print(f'{item_i}->{item_j}:{guess_text}')
            except Exception:
                pass


if __name__ == '__main__':
    main()
