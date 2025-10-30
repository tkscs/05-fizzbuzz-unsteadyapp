
today = "Monday"
# schoolday = today in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
schoolday = (
    (today == "Monday") or
    (today == "Tuesday") or
    (today == "Wednesday") or
    (today == "Thursday") or
    (today == "Friday")
)

if schoolday:
    if today == "Friday":
        print("We have Kab Shab today.")
    elif today == "Monday":
        print("We have Assembly today.")
    elif today == "Wednesday":
        print("We have Heart Work today.")
    else:
        print("We have a short break today.")
else:
    print("Weekend!!")