import ipdb; 

if __name__ == '__main__':
    N = int(input())
    list_ = []
    #ipdb.set_trace()

    for i in range(N):
        input_ = input().split()
        op = input_[0]

        if op == 'insert':
            list_.insert(int(input_[1]), int(input_[2]))
        elif op == 'print':
            print(list_)
        elif op == 'remove':
            list_.remove(int(input_[1]))
        elif op == 'append':
            list_.append(int(input_[1]))
        elif op == 'sort':
            list_.sort()
        elif op == 'pop':
            list_.pop()
        elif op == 'reverse':
            list_.reverse()