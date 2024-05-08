def pass_gen():
    import string, random
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

def main():
    print("Enter the number of passwords you want to generate:")
    num = int(input())
    for i in range(num):
        password = pass_gen()
        print("\nPassword {}: {}".format(i+1,password))
        
if __name__ == "__main__":
    main()