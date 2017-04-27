# ScanLine test data

test_ScanLine_first_KnobReadback = \
    [[[-3, -3, 0.0, 0.0], [-3, -3, 1.0, 1.0], [-3, -3, 2.0, 2.0]],
     [[-2, -2, 0.0, 0.0], [-2, -2, 1.0, 1.0], [-2, -2, 2.0, 2.0]],
     [[-1, -1, 0.0, 0.0], [-1, -1, 1.0, 1.0], [-1, -1, 2.0, 2.0]],
     [[0, 0, 0.0, 0.0], [0, 0, 1.0, 1.0], [0, 0, 2.0, 2.0]]]

test_ScanLine_first_Validation = \
    [[[], [], []], [[], [], []], [[], [], []], [[], [], []]]

test_ScanLine_first_Observable = \
    [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
     [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
     [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
     [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]]]

test_ScanLine_second_KnobReadback = \
    [[[[-3, -3, 0.0, 0.0], [-3, -3, 0.0, 0.0], [-3, -3, 0.0, 0.0], [-3, -3, 0.0, 0.0]],
      [[-3, -3, 1.0, 1.0], [-3, -3, 1.0, 1.0], [-3, -3, 1.0, 1.0], [-3, -3, 1.0, 1.0]],
      [[-3, -3, 2.0, 2.0], [-3, -3, 2.0, 2.0], [-3, -3, 2.0, 2.0], [-3, -3, 2.0, 2.0]]],
     [[[-2, -2, 0.0, 0.0], [-2, -2, 0.0, 0.0], [-2, -2, 0.0, 0.0], [-2, -2, 0.0, 0.0]],
      [[-2, -2, 1.0, 1.0], [-2, -2, 1.0, 1.0], [-2, -2, 1.0, 1.0], [-2, -2, 1.0, 1.0]],
      [[-2, -2, 2.0, 2.0], [-2, -2, 2.0, 2.0], [-2, -2, 2.0, 2.0], [-2, -2, 2.0, 2.0]]],
     [[[-1, -1, 0.0, 0.0], [-1, -1, 0.0, 0.0], [-1, -1, 0.0, 0.0], [-1, -1, 0.0, 0.0]],
      [[-1, -1, 1.0, 1.0], [-1, -1, 1.0, 1.0], [-1, -1, 1.0, 1.0], [-1, -1, 1.0, 1.0]],
      [[-1, -1, 2.0, 2.0], [-1, -1, 2.0, 2.0], [-1, -1, 2.0, 2.0], [-1, -1, 2.0, 2.0]]],
     [[[0, 0, 0.0, 0.0], [0, 0, 0.0, 0.0], [0, 0, 0.0, 0.0], [0, 0, 0.0, 0.0]],
      [[0, 0, 1.0, 1.0], [0, 0, 1.0, 1.0], [0, 0, 1.0, 1.0], [0, 0, 1.0, 1.0]],
      [[0, 0, 2.0, 2.0], [0, 0, 2.0, 2.0], [0, 0, 2.0, 2.0], [0, 0, 2.0, 2.0]]]]

test_ScanLine_second_Validation = \
    [[[[], [], [], []], [[], [], [], []], [[], [], [], []]], [[[], [], [], []], [[], [], [], []], [[], [], [], []]],
     [[[], [], [], []], [[], [], [], []], [[], [], [], []]], [[[], [], [], []], [[], [], [], []], [[], [], [], []]]]

test_ScanLine_second_Observable = \
    [[[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]]],
     [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]]],
     [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]]],
     [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]],
      [["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]]]]

# ScanSeries test data

test_ScanSeries_first_KnobReadback = \
    [[[[[-3, "1.2", 0, "2.2"], [-3, "1.2", 1, "2.2"], [-3, "1.2", 2, "2.2"]],
       [[-3, "1.2", "2.1", 0], [-3, "1.2", "2.1", 1]]],
      [[[-2, "1.2", 0, "2.2"], [-2, "1.2", 1, "2.2"], [-2, "1.2", 2, "2.2"]],
       [[-2, "1.2", "2.1", 0], [-2, "1.2", "2.1", 1]]],
      [[[-1, "1.2", 0, "2.2"], [-1, "1.2", 1, "2.2"], [-1, "1.2", 2, "2.2"]],
       [[-1, "1.2", "2.1", 0], [-1, "1.2", "2.1", 1]]],
      [[[0, "1.2", 0, "2.2"], [0, "1.2", 1, "2.2"], [0, "1.2", 2, "2.2"]],
       [[0, "1.2", "2.1", 0], [0, "1.2", "2.1", 1]]]], [
         [[["1.1", -3, 0, "2.2"], ["1.1", -3, 1, "2.2"], ["1.1", -3, 2, "2.2"]],
          [["1.1", -3, "2.1", 0], ["1.1", -3, "2.1", 1]]],
         [[["1.1", -2, 0, "2.2"], ["1.1", -2, 1, "2.2"], ["1.1", -2, 2, "2.2"]],
          [["1.1", -2, "2.1", 0], ["1.1", -2, "2.1", 1]]],
         [[["1.1", -1, 0, "2.2"], ["1.1", -1, 1, "2.2"], ["1.1", -1, 2, "2.2"]],
          [["1.1", -1, "2.1", 0], ["1.1", -1, "2.1", 1]]],
         [[["1.1", 0, 0, "2.2"], ["1.1", 0, 1, "2.2"], ["1.1", 0, 2, "2.2"]],
          [["1.1", 0, "2.1", 0], ["1.1", 0, "2.1", 1]]]]]

test_ScanSeries_first_Validation = \
    [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
     [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]]

test_ScanSeries_first_Observable = \
    [[[[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]],
      [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]],
      [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]],
      [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]],
     [[[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]],
      [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]],
      [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]],
      [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]]]


test_ScanSeries_second_KnobReadback = \
[[[[[[-3, "1.2", 0, "2.2"], [-3, "1.2", 0, "2.2"]], [[-3, "1.2", 1, "2.2"], [-3, "1.2", 1, "2.2"]], [[-3, "1.2", 2, "2.2"], [-3, "1.2", 2, "2.2"]]], [[[-3, "1.2", "2.1", 0], [-3, "1.2", "2.1", 0]], [[-3, "1.2", "2.1", 1], [-3, "1.2", "2.1", 1]]]], [[[[-2, "1.2", 0, "2.2"], [-2, "1.2", 0, "2.2"]], [[-2, "1.2", 1, "2.2"], [-2, "1.2", 1, "2.2"]], [[-2, "1.2", 2, "2.2"], [-2, "1.2", 2, "2.2"]]], [[[-2, "1.2", "2.1", 0], [-2, "1.2", "2.1", 0]], [[-2, "1.2", "2.1", 1], [-2, "1.2", "2.1", 1]]]], [[[[-1, "1.2", 0, "2.2"], [-1, "1.2", 0, "2.2"]], [[-1, "1.2", 1, "2.2"], [-1, "1.2", 1, "2.2"]], [[-1, "1.2", 2, "2.2"], [-1, "1.2", 2, "2.2"]]], [[[-1, "1.2", "2.1", 0], [-1, "1.2", "2.1", 0]], [[-1, "1.2", "2.1", 1], [-1, "1.2", "2.1", 1]]]], [[[[0, "1.2", 0, "2.2"], [0, "1.2", 0, "2.2"]], [[0, "1.2", 1, "2.2"], [0, "1.2", 1, "2.2"]], [[0, "1.2", 2, "2.2"], [0, "1.2", 2, "2.2"]]], [[[0, "1.2", "2.1", 0], [0, "1.2", "2.1", 0]], [[0, "1.2", "2.1", 1], [0, "1.2", "2.1", 1]]]]], [[[[["1.1", -3, 0, "2.2"], ["1.1", -3, 0, "2.2"]], [["1.1", -3, 1, "2.2"], ["1.1", -3, 1, "2.2"]], [["1.1", -3, 2, "2.2"], ["1.1", -3, 2, "2.2"]]], [[["1.1", -3, "2.1", 0], ["1.1", -3, "2.1", 0]], [["1.1", -3, "2.1", 1], ["1.1", -3, "2.1", 1]]]], [[[["1.1", -2, 0, "2.2"], ["1.1", -2, 0, "2.2"]], [["1.1", -2, 1, "2.2"], ["1.1", -2, 1, "2.2"]], [["1.1", -2, 2, "2.2"], ["1.1", -2, 2, "2.2"]]], [[["1.1", -2, "2.1", 0], ["1.1", -2, "2.1", 0]], [["1.1", -2, "2.1", 1], ["1.1", -2, "2.1", 1]]]], [[[["1.1", -1, 0, "2.2"], ["1.1", -1, 0, "2.2"]], [["1.1", -1, 1, "2.2"], ["1.1", -1, 1, "2.2"]], [["1.1", -1, 2, "2.2"], ["1.1", -1, 2, "2.2"]]], [[["1.1", -1, "2.1", 0], ["1.1", -1, "2.1", 0]], [["1.1", -1, "2.1", 1], ["1.1", -1, "2.1", 1]]]], [[[["1.1", 0, 0, "2.2"], ["1.1", 0, 0, "2.2"]], [["1.1", 0, 1, "2.2"], ["1.1", 0, 1, "2.2"]], [["1.1", 0, 2, "2.2"], ["1.1", 0, 2, "2.2"]]], [[["1.1", 0, "2.1", 0], ["1.1", 0, "2.1", 0]], [["1.1", 0, "2.1", 1], ["1.1", 0, "2.1", 1]]]]]]

test_ScanSeries_second_Validation = \
[[[[[[], []], [[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []], [[], []]], [[[], []], [[], []]]]], [[[[[], []], [[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []], [[], []]], [[[], []], [[], []]]]]]

test_ScanSeries_second_Observable = \
[[[[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]], [[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]], [[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]], [[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]]], [[[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]], [[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]], [[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]], [[[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]]]]

# ScanMixed test data

test_ScanMixed_first_KnobReadback = \
[[[[-3, -3, 0, "2.2"], [-3, -3, 1, "2.2"], [-3, -3, 2, "2.2"]], [[-3, -3, "2.1", 0], [-3, -3, "2.1", 1]]], [[[-2, -2, 0, "2.2"], [-2, -2, 1, "2.2"], [-2, -2, 2, "2.2"]], [[-2, -2, "2.1", 0], [-2, -2, "2.1", 1]]], [[[-1, -1, 0, "2.2"], [-1, -1, 1, "2.2"], [-1, -1, 2, "2.2"]], [[-1, -1, "2.1", 0], [-1, -1, "2.1", 1]]], [[[0, 0, 0, "2.2"], [0, 0, 1, "2.2"], [0, 0, 2, "2.2"]], [[0, 0, "2.1", 0], [0, 0, "2.1", 1]]]]

test_ScanMixed_first_Validation = \
[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]

test_ScanMixed_first_Observable = \
[[[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]]

test_ScanMixed_second_KnobReadback = \
[[[[-3, -3, 0, "2.2"], [-3, -3, 1, "2.2"], [-3, -3, 2, "2.2"]], [[-3, -3, "2.1", 0], [-3, -3, "2.1", 1]]], [[[-2, -2, 0, "2.2"], [-2, -2, 1, "2.2"], [-2, -2, 2, "2.2"]], [[-2, -2, "2.1", 0], [-2, -2, "2.1", 1]]], [[[-1, -1, 0, "2.2"], [-1, -1, 1, "2.2"], [-1, -1, 2, "2.2"]], [[-1, -1, "2.1", 0], [-1, -1, "2.1", 1]]], [[[0, 0, 0, "2.2"], [0, 0, 1, "2.2"], [0, 0, 2, "2.2"]], [[0, 0, "2.1", 0], [0, 0, "2.1", 1]]]]

test_ScanMixed_second_Validation = \
[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]

test_ScanMixed_second_Observable = \
[[[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]], [[["READ4", "READ5"], ["READ4", "READ5"], ["READ4", "READ5"]], [["READ4", "READ5"], ["READ4", "READ5"]]]]


# Yes, I'm ashamed. But unfortunately, no better way to test for the correct pre-allocation of the output.
test_output_format_expected_result = \
    [[[[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
       [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
       [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
       [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]],
      [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
       [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
       [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
       [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]]], [
         [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]],
         [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]]], [
         [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]],
         [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]]], [
         [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]],
         [[[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]],
          [[[[], [], []], [[], []]], [[[], [], []], [[], []]], [[[], [], []], [[], []]]]]]]

# Simple scan test
test_SimpleScan_first_KnobReadback = [-3, -2, -1, 0]
test_SimpleScan_first_Validation = [[], [], [], []]
test_SimpleScan_first_Observable = ["READ1", "READ1", "READ1", "READ1"]

test_SimpleScan_second_KnobReadback = [[-3, -3, -3], [-2, -2, -2], [-1, -1, -1], [0, 0, 0]]
test_SimpleScan_second_Validation = [[[], [], []], [[], [], []], [[], [], []], [[], [], []]]
test_SimpleScan_second_Observable = [['READ1', 'READ1', 'READ1'], ['READ1', 'READ1', 'READ1'], ['READ1', 'READ1', 'READ1'], ['READ1', 'READ1', 'READ1']]