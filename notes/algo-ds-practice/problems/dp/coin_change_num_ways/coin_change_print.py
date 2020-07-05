permutations = []


def coin_change(denominations, target_value, selected):
    if target_value < 0 or not denominations:
        return 0
    if target_value == 0:
        permutations.append(selected)
        return 1
    ans = 0
    # Include the last denominations at least 1 time
    selected_new = dict(selected)
    selected_new[denominations[-1]] += 1
    ans += coin_change(denominations, target_value - denominations[-1], selected_new)
    # Exclude the last denomination
    ans += coin_change(denominations[0:-1], target_value, selected)
    return ans


def print_selection(selection):
    output = ''
    for denom in selection:
        freq = selection[denom]
        if freq:
            output += str(denom) + 'x' + str(freq) + ' + '
    return output


def print_permutations():
    global permutations
    output = ''
    for perm in permutations:
        output += print_selection(perm) + '\n'
    return output


def main():
    dens = [2, 3, 5, 6]
    target_value = 10
    selected = {}
    for den in dens:
        selected[den] = 0
    ans = coin_change(dens, target_value, selected)
    print(ans)
    print(print_permutations())


if __name__ == "__main__":
    main()