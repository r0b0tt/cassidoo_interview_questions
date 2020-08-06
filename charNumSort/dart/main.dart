main() {
  List<String> myList = ["Bananas", "do", "not", "grow", "in", "Mississippi"];
  charNumSort(myList);
}

/// Prints an array that has been sorted based on the number
/// of distinct characters that occur in the word.
/// https://api.dart.dev/stable/2.9.0/dart-core/List/sort.html
charNumSort(List<String> myList) {
  myList.sort((a, b) => distinctCharacters(a, b));
  myList.sort((a, b) => a.length.compareTo(b.length));
  print(myList);
}

/// Compare function that uses the number of distinct characters
distinctCharacters(String a, String b) {
  List<String> a_characters = [], b_characters = [];

  for (var i = 0; i < a.length; i++) {
    if (!a_characters.contains(a[i])) {
      a_characters.add(a[i]);
    }
  }
  for (var i = 0; i < b.length; i++) {
    if (!b_characters.contains(b[i])) {
      b_characters.add(b[i]);
    }
  }

  return a_characters.length.compareTo(b_characters.length);
}
