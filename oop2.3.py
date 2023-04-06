with open('1.txt', encoding='utf-8') as file1:
    f1 = file1.readlines()
    words = [f1]
    with open('2.txt', encoding='utf-8') as file2:
        f2 = file2.readlines()
        words += [f2]
        with open('3.txt', encoding='utf-8') as file3:
            f3 = file3.readlines()
            words += [f3]
            words.sort(reverse=True)
            with open('end.txt', 'w') as end:
                for i in words:
                    if i == f1:
                        end.write('имя - 1.txt\n')
                    elif i == f2:
                        end.write('имя - 2.txt\n')
                    elif i == f3:
                        end.write('имя - 3.txt\n')
                    end.write(f'длинна - {len(i)}\n')
                    end.write(''.join(i))
                    end.write('\n')
