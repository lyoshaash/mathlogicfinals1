from turing_machine import TuringMachine

transitions = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', 'a'): ('q_bad_r', 'a', 'R'),
    ('q0', 'b'): ('q_bad_r', 'b', 'R'),
    ('q0', ' '): ('q_good_l', ' ', 'L'),

    ('q_bad_r', '0'): ('q_bad_r', '0', 'R'),
    ('q_bad_r', '1'): ('q_bad_r', '1', 'R'),
    ('q_bad_r', 'a'): ('q_bad_r', 'a', 'R'),
    ('q_bad_r', 'b'): ('q_bad_r', 'b', 'R'),
    ('q_bad_r', ' '): ('q_bad_l', ' ', 'L'),
    ('q_bad_l', '0'): ('q_bad_l', ' ', 'L'),
    ('q_bad_l', '1'): ('q_bad_l', ' ', 'L'),
    ('q_bad_l', 'a'): ('q_bad_l', ' ', 'L'),
    ('q_bad_l', 'b'): ('q_bad_l', ' ', 'L'),
    ('q_bad_l', ' '): ('q_write0', ' ', 'R'),


    ('q_good_l', '0'): ('q_good_l', ' ', 'L'),
    ('q_good_l', '1'): ('q_good_l', ' ', 'L'),
    ('q_good_l', ' '): ('q_write1', ' ', 'R'),


    ('q_write0', ' '): ('qa', '0', 'R'),
    ('q_write1', ' '): ('qa', '1', 'R'),
}

tm = TuringMachine(
    transitions=transitions,
    start_state='q0',
    accept_state='qa',
    reject_state=None,
    blank_symbol=' '
)

input_word = "01010101aba01010101"

final_tape = None
for _, tape_dict in tm.run(input_word):
    final_tape = tape_dict

left = final_tape['left_hand_side']
middle = final_tape['symbol']
right = final_tape['right_hand_side']
full_tape = ''.join(reversed(left)) + middle + ''.join(right)
output = full_tape.strip()

print("Вход:", input_word)
print("Выход:", output)
