'''
for i in range(5):
    for j in range(7):
        print(f'square{j+1}{i+1} = tk.Label(frame_container_right, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, relief="ridge", anchor="center").grid(row={j}, column={i})')
'''
for i in range(5):
    for j in range(7):
        print(f'square{j+1}{i+1} = tk.Label(frame_container_right, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, relief="ridge", anchor="center")','\n',f'square{j+1}{i+1}.grid(row={j}, column={i})')
'''
for i in range(5):
    for j in range(7):
        print(f'square{j+1}{i+1}.grid(row={j}, column={i})')
'''