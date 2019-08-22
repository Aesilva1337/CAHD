import 'package:flutter/material.dart';

class Classificacao extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('ExpansionTile'),
        ),
        body: ListView.builder(
          itemBuilder: (BuildContext context, int index) =>
              EntryItem(data[index]),
          itemCount: data.length,
        ),
      ),
    );
  }
}

// One entry in the multilevel list displayed by this app.
class Entry {
  Entry(this.title, this.type, [this.children = const <Entry>[]]);

  final dynamic type;
  final String title;
  final List<Entry> children;
}

// The entire multilevel list displayed by this app.
final List<Entry> data = <Entry>[
  Entry(
    'Sudorese (Hipoglicemia)',
    <Entry>[
      Entry('Item A0.1'),
      Entry('Item A0.2'),
      Entry('Item A0.3'),
    ],
  ),
  Entry('Alteração mental (hipo-hiperglicemia)', <Entry>[]),
  Entry('Febre'),
  Entry('Pulso anormal'),
  Entry('Vômito'),
  Entry('Visão borrada'),
  Entry('Dispnéia'),
  Entry(
    'Section A0',
    <Entry>[
      Entry('Item A0.1'),
      Entry('Item A0.2'),
      Entry('Item A0.3'),
    ],
  ),
];

// Displays one Entry. If the entry has children then it's displayed
// with an ExpansionTile.
class EntryItemState extends State<EntryItem> {
  SingingCharacter character = SingingCharacter.jefferson;

  EntryItemState(this.entry);

  final Entry entry;

  Widget _buildTiles(Entry root) {
    if (root.children.isEmpty)
      return RadioListTile<SingingCharacter>(
        title: const Text('Thomas Jefferson'),
        value: root.title == "Item A0.1"
            ? SingingCharacter.jefferson
            : SingingCharacter.lafayette,
        groupValue: character,
        onChanged: (SingingCharacter value) {
          setState(() {
            character = value;
          });
        },
      );
    return ExpansionTile(
      key: PageStorageKey<Entry>(root),
      title: Text(root.title),
      leading: Checkbox(
        onChanged: (bool checks) {},
        value: false,
      ),
      children: root.children.map(_buildTiles).toList(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return _buildTiles(entry);
  }
}

class EntryItem extends StatefulWidget {
  final Entry entry;
  const EntryItem(this.entry);
  @override
  EntryItemState createState() => EntryItemState(this.entry);
}

enum SingingCharacter { lafayette, jefferson }
