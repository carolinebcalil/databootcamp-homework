import os
import csv


months = []
pnl_changes = []

count_months = 0
net_pnl = 0
previous_month_pnl = 0
current_month_pnl = 0
pnl_change = 0


filepath = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(filepath, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
             
    for row in csv_reader:

        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_pnl = int(row[1])
        net_pnl += current_month_pnl

        if (count_months == 1):
            previous_month_pnl = current_month_pnl
            continue

        else:

            pnl_change = current_month_pnl - previous_month_pnl

            months.append(row[0])

            pnl_changes.append(pnl_change)

            previous_month_pnl = current_month_pnl

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_pnl = sum(pnl_changes)
    average_pnl = round(sum_pnl/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(pnl_changes)
    lowest_change = min(pnl_changes)

    #The greatest decrease in losses (date and amount) over the entire period
    highest_month_index = pnl_changes.index(highest_change)
    lowest_month_index = pnl_changes.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_pnl}")
print(f"Average Change:  ${average_pnl}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Export a text file 
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_pnl}\n")
    outfile.write(f"Average Change:  ${average_pnl}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")