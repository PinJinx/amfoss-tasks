import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:shared_preferences/shared_preferences.dart';

class DescriptionPage extends StatefulWidget {
  final int index;
  final List<dynamic> items;

  const DescriptionPage({super.key, required this.index, required this.items});

  @override
  State<DescriptionPage> createState() => _DescriptionPageState();
}

class _DescriptionPageState extends State<DescriptionPage> {
  @override
  void initState() {
    super.initState();
  }
  @override
  Widget build(BuildContext context) {
    var Data = widget.items[widget.index];
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text(Data["name"].toString()), // Convert to String if needed
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Container(
            height: (MediaQuery.sizeOf(context).height) * 0.3,
            width: (MediaQuery.sizeOf(context).width) * 0.5,
            decoration: BoxDecoration(
              image: DecorationImage(image: NetworkImage(Data["images"]["md"])),
              boxShadow: [
                BoxShadow(
                  color: const Color(0x3737373d).withOpacity(0.11),
                  blurRadius: 40,
                  spreadRadius: 0.0,
                )
              ],
            ),
          ),
          const Text(
            "Power Stats",
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          Text.rich(
            TextSpan(
              children: [
                const TextSpan(
                  text: "Intelligence: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["powerstats"]["intelligence"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "  Strength: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["powerstats"]["strength"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\nSpeed: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["powerstats"]["speed"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "  Durability: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["powerstats"]["durability"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\nPower: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["powerstats"]["power"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "  Combat: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["powerstats"]["combat"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
              ],
            ),
            textAlign: TextAlign.center,
          ),
          const Text(
            "Biography",
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          Text.rich(
            TextSpan(
              children: [
                const TextSpan(
                  text: "Full Name: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["biography"]["fullName"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\nAlter Egos: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["biography"]["alterEgos"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\nPlace of Birth: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["biography"]["placeOfBirth"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\nPublisher: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["biography"]["publisher"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\nFirst Appearance: ",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["biography"]["firstAppearance"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
              ],
            ),
            textAlign: TextAlign.center,
          ),
          const Text(
            "Connections",
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          Text.rich(
            TextSpan(
              children: [
                const TextSpan(
                  text: "Group Affiliation:\n",
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["connections"]["groupAffiliation"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
                const TextSpan(
                  text: "\n\nRelatives:\n",
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                TextSpan(
                  text: Data["connections"]["relatives"].toString(),
                  style: const TextStyle(color: Colors.black),
                ),
              ],
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),

    );
  }
}
