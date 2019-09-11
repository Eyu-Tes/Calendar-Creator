import calendar

print()
print(' Annual Calendar Creator '.center(50, '_'))

while True:
    try:
        yr = int(input('\nEnter the year to create calendar: '))
        if yr < 0:
            # raise User defined Exception, if -ve number is entered.
            raise Exception("Year can only be a positive number.")
    except ValueError:
        # Catches Exception if a non numeral is entered.
        print('Invalid year format, Enter again.')
    except Exception as err:
        # catches user defined Exception.
        print(err)
    else:
        file_name = f'{yr}-calendar.html'
        # create complete HTML page calendar.
        # start of the month will be Sunday.
        hc = calendar.HTMLCalendar(calendar.SUNDAY)
        # opens 2 files in a single statement & assign them to d|t file objects.
        with open(file_name, 'w') as f, open('static/layout.txt') as layout:
            header = layout.read()
            # Insert text from the other file to the html file.
            f.write(header)

            for mon in range(1, 13):
                # return a formatted month as table for the given year & month.
                txt = hc.formatmonth(yr, mon)
                # write into the html file.
                f.write(txt)
        print(f'\nCalendar created for {yr}.')
        print(f'Open --> {file_name}')
        break
