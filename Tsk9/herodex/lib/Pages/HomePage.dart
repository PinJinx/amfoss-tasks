import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:herodex/Pages/Description.dart';
import 'package:shared_preferences/shared_preferences.dart';

List<bool> Buttons_state = [false,false,false,true];
String Saved_data = "";
bool Fav_list_enabled = false;
bool DarkMode_enabled = false;
int Click_Index = 0;
String Fav_Link = 'Assets/Icons/List.svg';
Color BackDrop = Colors.white;
Color Button_Col = Colors.black;

class HomePage extends StatefulWidget {
  final List<dynamic> items;
  const HomePage({super.key, required this.items});
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<dynamic> f_items = [];
  SharedPreferences? prefs;
  @override
  void initState() {
    super.initState();
    f_items = widget.items; // Initialize f_items with all items
    initializePreferences();
  }
  Future<void> initializePreferences() async {
    prefs = await SharedPreferences.getInstance();
    String existingData = prefs?.getString("data") ?? "";
    if (existingData == ""){
      prefs?.setString("data", "");
    }
    else{
      setState(() {
        Saved_data = existingData;
      });
    }
     // Set initial data if needed
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbar(),
      backgroundColor: BackDrop,
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _searchField(),
          const SizedBox(height: 20),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              GestureDetector(
                  child: Container(
                    width: (MediaQuery.sizeOf(context).width)/4 - 10,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                        color: Buttons_state[0]? Colors.blue : Colors.transparent,
                        border: Border.all(color: Button_Col)
                    ),
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: Text(
                          "Hero",
                          style: TextStyle(
                            color: Button_Col,
                            fontSize: 18,
                            fontWeight: FontWeight.w600,
                          )
                      ),
                    ),
                  ),
                onTap: (){
                  setState(() {
                    Buttons_state[0] = true;
                    Buttons_state[1] = false;
                    Buttons_state[2] = false;
                    Buttons_state[3] = false;
                    f_items = [];
                    for (int i = 0; i < widget.items.length; i++) {
                      if (widget.items[i]["biography"]["alignment"] == "good") {
                        f_items.add(widget.items[i]);
                      }
                    }
                  });
                }
              ),
              GestureDetector(
                child: Container(
                  width: (MediaQuery.sizeOf(context).width)/4 - 10,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                      color: Buttons_state[1]? Colors.blue : Colors.transparent,
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(color: Button_Col)
                  ),
                  child: FittedBox(
                    fit: BoxFit.scaleDown,
                    child: Text(
                        "Anti-Hero",
                        style: TextStyle(
                          color: Button_Col,
                          fontSize: 18,
                          fontWeight: FontWeight.w600,
                        )
                    ),
                  ),
                ),
                  onTap: (){
                    setState(() {
                      f_items = [];
                      Buttons_state[1] = true;
                      Buttons_state[3] = false;
                      Buttons_state[2] = false;
                      Buttons_state[0] = false;
                      for (int i = 0; i < widget.items.length; i++) {
                        if (widget.items[i]["biography"]["alignment"] == "bad") {
                          f_items.add(widget.items[i]);
                        }
                      }
                    });
                  }
              ),
              GestureDetector(
                child: Container(
                  width: (MediaQuery.sizeOf(context).width)/4 - 10,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                      color: Buttons_state[2]? Colors.blue : Colors.transparent,
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(color: Button_Col)

                  ),

                  child: FittedBox(
                    fit: BoxFit.scaleDown,
                    child: Text(
                        "Villain",
                        style: TextStyle(
                          color: Button_Col,
                          fontSize: 18,
                          fontWeight: FontWeight.w600,
                        )
                    ),
                  ),
                ),
                  onTap: (){
                    setState(() {
                      Buttons_state[2] = true;
                      Buttons_state[1] = false;
                      Buttons_state[3] = false;
                      Buttons_state[0] = false;
                      f_items = [];
                      for (int i = 0; i < widget.items.length; i++) {
                        if (widget.items[i]["biography"]["alignment"] == "-") {
                          f_items.add(widget.items[i]);
                        }
                      }
                    });
                  }
              ),
              GestureDetector(
                  child: Container(
                    width: (MediaQuery.sizeOf(context).width)/4 - 10,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                        color: Buttons_state[3]? Colors.blue : Colors.transparent,
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(color: Button_Col)
                    ),
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: Text(
                          "All Characters",
                          style: TextStyle(
                            color: Button_Col,
                            fontSize: 18,
                            fontWeight: FontWeight.w600,
                          )
                      ),
                    ),
                  ),
                  onTap: (){
                    setState(() {
                      Buttons_state[3] = true;
                      Buttons_state[1] = false;
                      Buttons_state[2] = false;
                      Buttons_state[0] = false;
                      f_items = widget.items;
                      }
                    );
                  }
              ),
            ],
          ),
          const SizedBox(height: 20),
          Padding(
            padding: const EdgeInsets.only(left: 20),
            child: Text(
              "All Heroes",
              style: TextStyle(
                color: Button_Col,
                fontSize: 18,
                fontWeight: FontWeight.w600,
              ),
            ),
          ),
          const SizedBox(height: 15),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: f_items.isNotEmpty
              ?GridView.builder(
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 3, // Number of columns
                  crossAxisSpacing: 10.0, // Space between columns
                  mainAxisSpacing: 10.0, // Space between rows
                  childAspectRatio: 1.0, // Aspect ratio of each item
                ),
                itemCount: f_items.length,
                itemBuilder: (context, index) {
                  return GestureDetector(
                    child: Container(
                      padding: EdgeInsets.all(8),
                      margin: EdgeInsets.symmetric(vertical: 5, horizontal: 5),
                      decoration: BoxDecoration(
                        color: Colors.grey,
                        image: DecorationImage(
                          image: NetworkImage(f_items[index]["images"]["md"]),
                          fit: BoxFit.fill,
                        ),
                        borderRadius: BorderRadius.circular(10),
                      ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: [
                            Align(
                              alignment: Alignment.topCenter,
                              child: Text(
                                f_items[index]["name"],
                                textAlign: TextAlign.center,
                                style: const TextStyle(
                                  backgroundColor: Colors.black54,
                                  fontSize: 10,
                                  color: Colors.white,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            Spacer(),
                            GestureDetector(
                              child: Align(
                                alignment: Alignment.bottomLeft,
                                child: SizedBox(
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: SvgPicture.asset(
                                      'Assets/Icons/Like.svg',
                                      height: 25,
                                      width: 25,
                                      colorFilter: ColorFilter.mode(Saved_data.contains('%${index.toString()}') ? Colors.pink : Colors.white,BlendMode.modulate),
                                      fit: BoxFit.scaleDown
                                    ),
                                  ),
                                ),
                              ),
                              onTap: () async {
                                prefs = await SharedPreferences.getInstance();
                                String existingData = prefs?.getString("data") ?? "";
                                if(existingData.contains("%$index")){
                                  String newData = existingData.replaceAll("%$index","");
                                  await prefs?.setString("data", newData);
                                  setState(() {
                                    Saved_data = newData;
                                  });
                                }
                                else{
                                  String newData = "$existingData%$index";
                                  await prefs?.setString("data", newData);
                                  setState(() {
                                    Saved_data = newData;
                                  });
                                }
                              },
                            )

                          ],
                        )

                    ),
                    onTap: (){
                      Navigator.push(context, MaterialPageRoute(
                        builder: (context)=> DescriptionPage(
                          index: index,
                          items: f_items,
                        ),
                      ));
                    },
                  );
                },
              )
                  : const Center(
                child: Text("No Data To Display!")
              ),
            ),
          ),
        ],
      ),
    );
  }



  Container _searchField() {
    return Container(
      margin: const EdgeInsets.only(top: 10, left: 20, right: 10),
      decoration: BoxDecoration(
        boxShadow: [
          BoxShadow(
            color: const Color(0x3737373d).withOpacity(0.11),
            blurRadius: 40,
            spreadRadius: 0.0,
          ),
        ],
      ),


      child: TextField(
        onChanged: (text) {
          setState(() {
            if (text.isEmpty) {
              f_items = widget.items; f_items = widget.items;// Reset to all items if search is empty
            } else {
              Buttons_state = [false,false,false,true];
              f_items = widget.items.where((item) {
                return item["name"]
                    .toString()
                    .toLowerCase()
                    .contains(text.toLowerCase());
              }).toList();
            }
          });
        },
        decoration: InputDecoration(
          hintText: "Search Heroes!",
          hintStyle: const TextStyle(fontSize: 14, color: Colors.grey),
          prefixIcon: Padding(
            padding: const EdgeInsets.all(12),
            child: SvgPicture.asset('Assets/Icons/Mag.svg'),
          ),
          filled: true,
          fillColor: Colors.white,
          contentPadding: const EdgeInsets.all(15),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(15),
            borderSide: BorderSide.none,
          ),
        ),
      ),
    );
  }
  AppBar appbar() {
    return AppBar(
      title: Text(
        'HeroDex!',
        style: TextStyle(
          color: Colors.black,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
      ),
      leading: GestureDetector(
        child: Container(
          margin: const EdgeInsets.all(15),
          child: SvgPicture.asset('Assets/Icons/gear.svg'),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(10),
          ),
        ),
        onTap: () {
          setState(() {
            DarkMode_enabled = !DarkMode_enabled;
            if(DarkMode_enabled){
              BackDrop = Colors.black;
              Button_Col = Colors.white;
            }
            else{
              BackDrop = Colors.white;
              Button_Col = Colors.black;
            }
          });
        },
      ),
      actions: [
        GestureDetector(
          child: Container(
            margin: const EdgeInsets.all(15),
            width: 47,
            child: SvgPicture.asset(Fav_Link),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(10),
            ),
          ),
          onTap: () {
            if(!Fav_list_enabled){
              setState(() {
                Fav_list_enabled = true;
                f_items = [];
                Fav_Link = 'Assets/Icons/Like.svg';
                for (int i = 0; i < widget.items.length; i++) {
                  String existingData = prefs?.getString("data") ?? "";
                  if (existingData.contains("%$i")) {
                    f_items.add(widget.items[i]);
                  }
                }
              });
            }
            else{
              setState(() {
                Fav_Link = 'Assets/Icons/List.svg';
                Fav_list_enabled = false;
                f_items = widget.items;
              });
            }
          },
        ),
      ],
      centerTitle: true,
      backgroundColor: Colors.white,
      elevation: 0.1,
    );
  }
}


