def decorator_main(func):
    def wrapper(ps):
        print(f'Before main {ps=}')
        print(str(func()))
        print(f'After main')
        print(ps)
    return wrapper

@decorator_main('∞')
def main():
    a = 'Practice with decorator'
    return a

main()