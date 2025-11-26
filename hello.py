print("Hello, Git world!") 

def greet(name):
    """Повертає привітання."""
    return f"Hello, {name} from FEATURE branch!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))