num_machines, num_workers, price, total_candies = map(int, input().split())
current_candies = 0
count = 0

while current_candies < total_candies:
    current_candies += num_machines * num_workers
    # Another check to avoid further computations
    if current_candies >= total_candies:
        count += 1
        break
    if current_candies > price:
        num = int(current_candies/price)
        passes_without_change = (total_candies - current_candies) / (num_machines * num_workers)
        if passes_without_change < 1:
            count += 1
            continue
        passes_with_change = passes_without_change
        i = 1
        purchases, w, m = i, num_workers, num_machines
        while i <= num:
            if w < m:
                w += 1
            else:
                m += 1
            w_c = (total_candies - (current_candies - (price * i))) / (m * w)
            if w_c < 1:
                passes_with_change, purchases = w_c, i
                break
            if w_c < passes_with_change:
                passes_with_change, purchases = w_c, i
            i += 1

        if passes_with_change < passes_without_change:
            num_machines, num_workers = m, w
            current_candies -= (price * purchases)

    count += 1

print(count)
