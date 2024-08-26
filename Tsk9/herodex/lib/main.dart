import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:herodex/Pages/HomePage.dart';
import 'package:flutter/services.dart' show rootBundle;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  Future<List<dynamic>> loadJsonAsset() async {
    final String jsonString = await rootBundle.loadString('Assets/Json/superhero.json');
    return json.decode(jsonString);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Hero Dex",
      debugShowCheckedModeBanner: false,
      home: FutureBuilder<List<dynamic>>(
        future: loadJsonAsset(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            // Show a loading indicator while the data is being loaded
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            // Handle any errors that occur during the data loading process
            return const Center(child: Text("An error occurred while loading data"));
          } else if (snapshot.hasData) {
            // Data is loaded, proceed to HomePage with the loaded items
            return HomePage(items: snapshot.data!);
          } else {
            // Handle the case where no data is loaded
            return const Center(child: Text("No data found"));
          }
        },
      ),
    );
  }
}
