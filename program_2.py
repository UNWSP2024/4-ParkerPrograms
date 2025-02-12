#Nathan Parker
#2/11/25
#Program #2: Movie Tix

#set tickets to 0
tickets = 0

#get the number of movies from the user
number_of_movies = int(input('Enter the number of movies you want to see: '))

#get the name and number of tickets for each movie and add additional tickets ordered to the accumulator
for number in range(number_of_movies):
    movies = input('Enter the name of the a movie for which you want tickets: ')
    additional_tickets = int(input(f'Enter the number of tickets that you want for {movies}: '))
    tickets += additional_tickets

#display the number of tickets ordered
if tickets == 1:
    print('You ordered', tickets, 'ticket.')
else:
    print('You ordered', tickets, 'tickets.')
