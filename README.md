appaboutpage 

weatherdisplay

socialmediapost

productshowcase

personalprofile

newsarticle

musicalbumdisplay

foodmenuitem

contactcard

Student-ID-Card

###1)Assignment 1: Student ID Card

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF2F4F7),
        body: Center(
          child: StudentIDCard(
            name: 'John Smith',
            id: '2024CS001',
            course: 'Computer Science',
            batch: '2024-2028',
            validTill: '2028',
          ),
        ),
      ),
    );
  }
}

class StudentIDCard extends StatelessWidget {
  final String name;
  final String id;
  final String course;
  final String batch;
  final String validTill;
  final ImageProvider? photo;

  const StudentIDCard({
    super.key,
    required this.name,
    required this.id,
    required this.course,
    required this.batch,
    required this.validTill,
    this.photo,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 320,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.2),
            blurRadius: 8,
            spreadRadius: 2,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // University header
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.school_rounded, color: Colors.amber, size: 24),
              const SizedBox(width: 6),
              Text(
                'Tech University',
                style: GoogleFonts.poppins(
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                  color: Colors.grey.shade800,
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),

          // Profile image placeholder
          CircleAvatar(
            radius: 36,
            backgroundColor: Colors.deepPurple.shade100,
            backgroundImage: photo,
            child: photo == null
                ? const Icon(Icons.person, color: Colors.deepPurple, size: 40)
                : null,
          ),
          const SizedBox(height: 14),

          // Name
          Text(
            name,
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: Colors.black87,
            ),
          ),
          const SizedBox(height: 6),

          // ID
          Text(
            'ID: $id',
            style: GoogleFonts.inter(
              fontWeight: FontWeight.w400,
              color: Colors.grey.shade700,
              fontSize: 14,
            ),
          ),
          const SizedBox(height: 6),

          // Course
          Text(
            course,
            style: GoogleFonts.inter(
              fontWeight: FontWeight.w400,
              color: Colors.grey.shade700,
              fontSize: 14,
            ),
          ),
          const SizedBox(height: 6),

          // Batch
          Text(
            'Batch: $batch',
            style: GoogleFonts.inter(
              fontWeight: FontWeight.w400,
              color: Colors.grey.shade700,
              fontSize: 14,
            ),
          ),
          const SizedBox(height: 12),

          // Validity
          Text(
            'Valid until $validTill',
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w500,
              color: Colors.grey.shade600,
              fontSize: 13,
            ),
          ),
        ],
      ),
    );
  }
}


###2)Assignment 2: Personal Profile

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF3F4F6),
        body: const Center(
          child: PersonalProfileCard(
            name: 'John Smith',
            bio: 'A passionate Flutter developer who loves to build elegant and functional mobile apps. Constant learner and open-source contributor.',
            followers: 1200,
            projects: 25,
            rating: 4.8,
          ),
        ),
      ),
    );
  }
}

class PersonalProfileCard extends StatelessWidget {
  final String name;
  final String bio;
  final int followers;
  final int projects;
  final double rating;

  const PersonalProfileCard({
    super.key,
    required this.name,
    required this.bio,
    required this.followers,
    required this.projects,
    required this.rating,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 320,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.2),
            blurRadius: 10,
            spreadRadius: 2,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Avatar
          CircleAvatar(
            radius: 40,
            backgroundColor: Colors.blue.shade100,
            child: const Icon(Icons.person, color: Colors.blue, size: 45),
          ),
          const SizedBox(height: 12),

          // Name
          Text(
            name,
            style: GoogleFonts.montserrat(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: Colors.black87,
            ),
          ),
          const SizedBox(height: 8),

          // Bio
          Text(
            bio,
            textAlign: TextAlign.center,
            style: GoogleFonts.openSans(
              fontWeight: FontWeight.w400,
              fontSize: 13,
              color: Colors.grey.shade700,
            ),
          ),
          const SizedBox(height: 16),

          // Divider
          Divider(color: Colors.grey.shade300, thickness: 1),

          const SizedBox(height: 12),

          // Stats Row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildStat('Followers', followers.toString()),
              _buildStat('Projects', projects.toString()),
              _buildStat('Rating', rating.toString()),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildStat(String label, String value) {
    return Column(
      children: [
        Text(
          value,
          style: GoogleFonts.roboto(
            fontWeight: FontWeight.w500,
            fontSize: 15,
            color: Colors.blue.shade800,
          ),
        ),
        const SizedBox(height: 4),
        Text(
          label,
          style: GoogleFonts.openSans(
            fontWeight: FontWeight.w400,
            fontSize: 12,
            color: Colors.grey.shade600,
          ),
        ),
      ],
    );
  }
}


###3) Assignment 3: Food Menu Item

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF5F6FA),
        body: const Center(
          child: FoodMenuCard(
            foodName: 'Margherita Pizza',
            description:
                'Fresh tomatoes, mozzarella cheese, basil leaves on crispy thin crust',
            price: '\$12.99',
          ),
        ),
      ),
    );
  }
}

class FoodMenuCard extends StatelessWidget {
  final String foodName;
  final String description;
  final String price;

  const FoodMenuCard({
    super.key,
    required this.foodName,
    required this.description,
    required this.price,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 260,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.15),
            blurRadius: 10,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Gradient Header with Pizza Emoji
          Container(
            height: 80,
            width: double.infinity,
            decoration: const BoxDecoration(
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(20),
                topRight: Radius.circular(20),
              ),
              gradient: LinearGradient(
                colors: [Color(0xFFFF8A00), Color(0xFFFF3D00)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
            child: const Center(
              child: Text(
                '🍕',
                style: TextStyle(fontSize: 40),
              ),
            ),
          ),

          // Content Section
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Food Name
                Text(
                  foodName,
                  style: GoogleFonts.playfairDisplay(
                    fontWeight: FontWeight.bold,
                    fontSize: 18,
                    color: Colors.black87,
                  ),
                ),
                const SizedBox(height: 6),

                // Description
                Text(
                  description,
                  style: GoogleFonts.lato(
                    fontWeight: FontWeight.w400,
                    fontSize: 13.5,
                    color: Colors.grey.shade700,
                  ),
                ),
                const SizedBox(height: 10),

                // Price
                Text(
                  price,
                  style: GoogleFonts.roboto(
                    fontWeight: FontWeight.bold,
                    fontSize: 15,
                    color: Colors.redAccent,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}


###4) Assignment 4: Weather Display

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF3F4F6),
        body: const Center(
          child: WeatherCard(
            temperature: 24,
            location: 'New York',
            description: 'Sunny',
            high: 28,
            low: 18,
          ),
        ),
      ),
    );
  }
}

class WeatherCard extends StatelessWidget {
  final int temperature;
  final String location;
  final String description;
  final int high;
  final int low;

  const WeatherCard({
    super.key,
    required this.temperature,
    required this.location,
    required this.description,
    required this.high,
    required this.low,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 260,
      padding: const EdgeInsets.symmetric(vertical: 26, horizontal: 18),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        gradient: const LinearGradient(
          colors: [Color(0xFF63A4FF), Color(0xFF83EAF1)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.blue.withOpacity(0.2),
            blurRadius: 10,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // ☀️ Weather Icon
          const Icon(
            Icons.wb_sunny_rounded,
            color: Colors.yellow,
            size: 52,
          ),
          const SizedBox(height: 10),

          // 🌡️ Temperature
          Text(
            '$temperature°',
            style: GoogleFonts.raleway(
              fontWeight: FontWeight.bold,
              fontSize: 42,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 4),

          // 📍 Location
          Text(
            location,
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w500,
              fontSize: 16,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 2),

          // ☀️ Description
          Text(
            description,
            style: GoogleFonts.openSans(
              fontWeight: FontWeight.w400,
              fontSize: 14,
              color: Colors.white70,
            ),
          ),
          const SizedBox(height: 18),

          // 🔽 High & Low row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'High: $high°',
                style: GoogleFonts.openSans(
                  fontWeight: FontWeight.w400,
                  fontSize: 13,
                  color: Colors.white,
                ),
              ),
              Text(
                'Low: $low°',
                style: GoogleFonts.openSans(
                  fontWeight: FontWeight.w400,
                  fontSize: 13,
                  color: Colors.white,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}


###5) Assignment 5: Product Showcase

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF3F4F6),
        body: Center(
          child: ProductShowcaseCard(
            productName: 'Air Zoom Pegasus 40',
            brand: 'Nike',
            price: '\$129.99',
          ),
        ),
      ),
    );
  }
}

class ProductShowcaseCard extends StatelessWidget {
  final String productName;
  final String brand;
  final String price;

  const ProductShowcaseCard({
    super.key,
    required this.productName,
    required this.brand,
    required this.price,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 260,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.15),
            blurRadius: 10,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // 👟 Product Icon
          const Text(
            '👟',
            style: TextStyle(fontSize: 48),
          ),
          const SizedBox(height: 12),

          // 🏷️ Product Name
          Text(
            productName,
            textAlign: TextAlign.center,
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: Colors.black87,
            ),
          ),
          const SizedBox(height: 6),

          // 🏢 Brand
          Text(
            brand,
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w500,
              fontSize: 14,
              color: Colors.grey.shade600,
            ),
          ),
          const SizedBox(height: 10),

          // 💰 Price
          Text(
            price,
            style: GoogleFonts.montserrat(
              fontWeight: FontWeight.bold,
              fontSize: 16,
              color: Colors.green.shade700,
            ),
          ),
        ],
      ),
    );
  }
}


###6) Assignment 6: News Article Preview

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF4F6F8),
        body: Center(
          child: NewsArticleCard(
            headline: 'AI Revolutionizes Healthcare Industry',
            description:
                'Artificial Intelligence is transforming patient care, diagnostics, and medical research with smarter algorithms and data-driven insights.',
            meta: '⏰ 2h ago · Tech News',
          ),
        ),
      ),
    );
  }
}

class NewsArticleCard extends StatelessWidget {
  final String headline;
  final String description;
  final String meta;

  const NewsArticleCard({
    super.key,
    required this.headline,
    required this.description,
    required this.meta,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 300,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.15),
            blurRadius: 8,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text('📰', style: TextStyle(fontSize: 36)),
          const SizedBox(height: 10),

          // 🗞️ Headline
          Text(
            headline,
            style: GoogleFonts.merriweather(
              fontWeight: FontWeight.bold,
              fontSize: 16,
              color: Colors.black87,
            ),
          ),
          const SizedBox(height: 8),

          // 📖 Description
          Text(
            description,
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w400,
              fontSize: 14,
              color: Colors.grey.shade700,
              height: 1.4,
            ),
          ),
          const SizedBox(height: 12),

          // ⏰ Meta
          Text(
            meta,
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w300,
              fontSize: 13,
              color: Colors.grey.shade600,
            ),
          ),
        ],
      ),
    );
  }
}


###7) Assignment 7: Social Media Post

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF5F6FA),
        body: const Center(
          child: SocialMediaPost(),
        ),
      ),
    );
  }
}

class SocialMediaPost extends StatelessWidget {
  const SocialMediaPost({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 330,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.20),
            blurRadius: 10,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Profile Row
          Row(
            children: [
              const CircleAvatar(
                radius: 22,
                backgroundColor: Color(0xFFFFE2A8),
                child: Text(
                  "🙂",
                  style: TextStyle(fontSize: 26),
                ),
              ),
              const SizedBox(width: 10),

              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Mike Chen",
                    style: GoogleFonts.poppins(
                      fontWeight: FontWeight.w600,
                      fontSize: 16,
                      color: Colors.black87,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    "2 hours ago",
                    style: GoogleFonts.roboto(
                      fontWeight: FontWeight.w300,
                      fontSize: 13,
                      color: Colors.grey,
                    ),
                  ),
                ],
              ),
            ],
          ),

          const SizedBox(height: 14),

          // Post Content
          Text(
            "Just finished building my first Flutter app! The widgets system is incredible 🚀",
            style: GoogleFonts.inter(
              fontWeight: FontWeight.w400,
              fontSize: 14,
              height: 1.5,
              color: Colors.black87,
            ),
          ),

          const SizedBox(height: 14),

          // Gradient Media Box
          Container(
            height: 120,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(16),
              gradient: const LinearGradient(
                colors: [
                  Color(0xFFE3F1FF),
                  Color(0xFFFCE8FF),
                ],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
            child: const Center(
              child: Text(
                "📱",
                style: TextStyle(fontSize: 40),
              ),
            ),
          ),

          const SizedBox(height: 14),

          // Likes + Comments
          Row(
            children: [
              const Icon(Icons.favorite, color: Colors.redAccent, size: 20),
              const SizedBox(width: 4),
              Text(
                "24 likes",
                style: GoogleFonts.inter(
                  fontWeight: FontWeight.w400,
                  fontSize: 13,
                  color: Colors.black87,
                ),
              ),
              const SizedBox(width: 20),
              const Icon(Icons.chat_bubble_outline,
                  color: Colors.purple, size: 20),
              const SizedBox(width: 4),
              Text(
                "8 comments",
                style: GoogleFonts.inter(
                  fontWeight: FontWeight.w400,
                  fontSize: 13,
                  color: Colors.black87,
                ),
              ),
            ],
          )
        ],
      ),
    );
  }
}


###8) Assignment 8: Music Album Display

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF3F4F6),
        body: const Center(
          child: MusicAlbumCard(
            title: 'Midnight Echoes',
            artist: 'Luna & The Waves',
            year: 2024,
            tracks: 12,
          ),
        ),
      ),
    );
  }
}

class MusicAlbumCard extends StatelessWidget {
  final String title;
  final String artist;
  final int year;
  final int tracks;

  const MusicAlbumCard({
    super.key,
    required this.title,
    required this.artist,
    required this.year,
    required this.tracks,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 300,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.08),
            blurRadius: 12,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Cover art placeholder with soft gradient + emoji
          Container(
            height: 150,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(16),
              gradient: const LinearGradient(
                colors: [Color(0xFF8EC5FC), Color(0xFFE0C3FC)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
            child: const Center(
              child: Text('🎶', style: TextStyle(fontSize: 48)),
            ),
          ),
          const SizedBox(height: 14),

          // 🎵 Album Title
          Text(
            title,
            textAlign: TextAlign.center,
            style: GoogleFonts.playfairDisplay(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: Colors.black87,
              height: 1.2,
            ),
          ),
          const SizedBox(height: 6),

          // 🎤 Artist
          Text(
            artist,
            textAlign: TextAlign.center,
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w500,
              fontSize: 14,
              color: Colors.grey.shade700,
            ),
          ),
          const SizedBox(height: 10),

          // 📅 Year/Tracks
          Text(
            'Released: $year  •  $tracks tracks',
            textAlign: TextAlign.center,
            style: GoogleFonts.openSans(
              fontWeight: FontWeight.w400,
              fontSize: 13,
              color: Colors.grey.shade600,
            ),
          ),
        ],
      ),
    );
  }
}


###9) Assignment 9: Contact Card

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFFF4F5F7),
        body: const Center(
          child: ContactCard(
            name: 'Emma Johnson',
            phone: '+1 202 555 0147',
            email: 'emma.johnson@example.com',
            address: '221B Baker Street, London, UK',
          ),
        ),
      ),
    );
  }
}

class ContactCard extends StatelessWidget {
  final String name;
  final String phone;
  final String email;
  final String address;

  const ContactCard({
    super.key,
    required this.name,
    required this.phone,
    required this.email,
    required this.address,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 310,
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14), // reduced padding
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.18),
            blurRadius: 8,
            offset: const Offset(0, 4),
          ),
        ],
      ),

      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min, // lets card shrink
        children: [
          // Top Row with Avatar + Name
          Row(
            children: [
              const CircleAvatar(
                radius: 24, // smaller avatar
                backgroundColor: Color(0xFFDCE7FF),
                child: Icon(Icons.person, color: Color(0xFF3A66FF), size: 28),
              ),
              const SizedBox(width: 12),

              Expanded(
                child: Text(
                  name,
                  style: GoogleFonts.montserrat(
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                    color: Colors.black87,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 10),

          // Phone Row
          Row(
            children: [
              const Icon(Icons.phone, size: 18, color: Colors.blueAccent),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  phone,
                  style: GoogleFonts.roboto(
                    fontWeight: FontWeight.w400,
                    fontSize: 13,
                    color: Colors.grey.shade800,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 6),

          // Email Row
          Row(
            children: [
              const Icon(Icons.email, size: 18, color: Colors.redAccent),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  email,
                  style: GoogleFonts.roboto(
                    fontWeight: FontWeight.w400,
                    fontSize: 13,
                    color: Colors.grey.shade800,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 6),

          // Address Row
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Icon(Icons.location_on, size: 18, color: Colors.deepPurple),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  address,
                  style: GoogleFonts.openSans(
                    fontWeight: FontWeight.w400,
                    fontSize: 13,
                    color: Colors.grey.shade700,
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}


###10) Assignment 10: App About Page

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const Scaffold(
        backgroundColor: Color(0xFFF5F6FA),
        body: Center(child: AboutCard()),
      ),
    );
  }
}

class AboutCard extends StatelessWidget {
  const AboutCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 330,
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.06),
            blurRadius: 16,
            offset: const Offset(0, 10),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // App icon (gradient square with emoji)
          Container(
            width: 80,
            height: 80,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(22),
              gradient: const LinearGradient(
                colors: [Color(0xFF6F7BF7), Color(0xFF7ED0FF)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
            child: const Center(
              child: Text('📱', style: TextStyle(fontSize: 34)),
            ),
          ),
          const SizedBox(height: 16),

          // App Name — Poppins bold
          Text(
            'MyFlutterApp',
            textAlign: TextAlign.center,
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.bold,
              fontSize: 22,
              color: Colors.black87,
            ),
          ),

          const SizedBox(height: 6),

          // Version — Inter w400 (light grey)
          Text(
            'Version 1.0.0',
            style: GoogleFonts.inter(
              fontWeight: FontWeight.w400,
              fontSize: 13.5,
              color: Colors.grey.shade600,
            ),
          ),

          const SizedBox(height: 18),

          // Description — Inter w400
          Text(
            'A beautiful mobile application built with Flutter. This app demonstrates clean UI design and smooth user experience with modern Material Design principles.',
            textAlign: TextAlign.center,
            style: GoogleFonts.inter(
              fontWeight: FontWeight.w400,
              fontSize: 14.5,
              height: 1.55,
              color: Colors.grey.shade800,
            ),
          ),

          const SizedBox(height: 18),

          Divider(color: Colors.grey.shade200, thickness: 1),

          const SizedBox(height: 12),

          // "Developer Information" title — Roboto w500
          Align(
            alignment: Alignment.centerLeft,
            child: Text(
              'Developer Information',
              style: GoogleFonts.roboto(
                fontWeight: FontWeight.w500,
                fontSize: 16,
                color: Colors.black87,
              ),
            ),
          ),
          const SizedBox(height: 10),

          // Info rows — Roboto w500 (as per assignment)
          _InfoRow(
            emoji: '📚',
            text: 'ABC Tech Solutions',
          ),
          const SizedBox(height: 8),
          _InfoRow(
            emoji: '📧',
            text: 'support@abctech.com',
          ),
          const SizedBox(height: 8),
          _InfoRow(
            emoji: '🌐',
            text: 'www.abctech.com',
          ),
        ],
      ),
    );
  }
}

class _InfoRow extends StatelessWidget {
  final String emoji;
  final String text;

  const _InfoRow({required this.emoji, required this.text});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Text(emoji, style: const TextStyle(fontSize: 18)),
        const SizedBox(width: 10),
        Expanded(
          child: Text(
            text,
            style: GoogleFonts.roboto(
              fontWeight: FontWeight.w500, // per assignment
              fontSize: 14,
              color: Colors.grey.shade800,
            ),
          ),
        ),
      ],
    );
  }
}


Assignmet 2:

Greeting Card:

import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Greeting Card',
      theme: ThemeData(primarySwatch: Colors.pink),
      home: const FirstScreen(),
    );
  }
}

// ✅ FIRST SCREEN
class FirstScreen extends StatefulWidget {
  const FirstScreen({super.key});

  @override
  State<FirstScreen> createState() => _FirstScreenState();
}

class _FirstScreenState extends State<FirstScreen> {
  final TextEditingController _nameController = TextEditingController();

  void _navigateToGreeting() {
    final name = _nameController.text.trim();
    if (name.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Please enter your name!")),
      );
    } else {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => GreetingScreen(name: name),
        ),
      );
    }
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.pink.shade50,
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                "Enter Your Name",
                style: GoogleFonts.poppins(
                  fontSize: 22,
                  fontWeight: FontWeight.w600,
                  color: Colors.pink.shade700,
                ),
              ),

              const SizedBox(height: 20),

              // ✅ Name TextField
              TextField(
                controller: _nameController,
                decoration: InputDecoration(
                  labelText: "Your Name",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                  filled: true,
                  fillColor: Colors.white,
                ),
              ),

              const SizedBox(height: 20),

              ElevatedButton(
                onPressed: _navigateToGreeting,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.pink.shade400,
                  padding: const EdgeInsets.symmetric(
                      horizontal: 30, vertical: 12),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10)),
                ),
                child: const Text(
                  "See Your Gift",
                  style: TextStyle(fontSize: 16, color: Colors.white),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// ✅ SECOND SCREEN WITH EMOJI INSTEAD OF IMAGE
class GreetingScreen extends StatelessWidget {
  final String name;
  const GreetingScreen({super.key, required this.name});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.pink.shade100,
      appBar: AppBar(
        title: const Text("Your Greeting Card"),
        backgroundColor: Colors.pink.shade400,
        centerTitle: true,
      ),

      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              // ✅ EMOJI ABOVE GREETING (NO IMAGE NEEDED)
              const Text(
                "🎂",
                style: TextStyle(fontSize: 100),
              ),

              const SizedBox(height: 20),

              // ✅ Lottie Animation
              Lottie.asset(
                'assets/birthday.json',
                width: 220,
                repeat: true,
              ),

              const SizedBox(height: 20),

              // ✅ Greeting Text
              Text(
                "Happy Birthday, $name!",
                style: GoogleFonts.pacifico(
                  fontSize: 30,
                  color: Colors.pink.shade800,
                ),
                textAlign: TextAlign.center,
              ),

              const SizedBox(height: 40),

              // ✅ Back Button
              ElevatedButton.icon(
                onPressed: () => Navigator.pop(context),
                icon: const Icon(Icons.arrow_back),
                label: const Text("Back"),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.pink.shade400,
                  padding: const EdgeInsets.symmetric(
                      horizontal: 24, vertical: 12),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}


##### In pubspec.yaml
    assets:
    - assets/birthday.json
    - assets/images/birthday.png

flutter pub add lottie

### birthday.json file
     {
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 120,
  "w": 500,
  "h": 500,
  "layers": [
    {
      "ddd": 0,
      "ind": 1,
      "ty": 4,
      "ks": {
        "o": { "a": 0, "k": 100 },
        "r": { "a": 1, "k": [ { "t": 0, "s": 0 }, { "t": 60, "s": 360 } ] }
      },
      "shapes": []
    }
  ]
}


    





