import json
import os


def enrich_azure_data():
    """
    Enriches azure_offline_data.json with more_info from azure_plugin_info_only.json
    based on matching Plugin Name
    """

    # File paths
    plugin_info_path = "gcp_plugin_info_only.json"
    offline_data_path = "google_offline_data.json"
    output_path = "gcp_offline_data_enriched.json"

    print("Loading plugin info data...")
    # Load the plugin info data (contains more_info field)
    with open(plugin_info_path, "r", encoding="utf-8") as f:
        plugin_info_data = json.load(f)

    print("Loading offline data...")
    # Load the offline data (to be enriched)
    with open(offline_data_path, "r", encoding="utf-8") as f:
        offline_data = json.load(f)

    # Create lookup dictionary from plugin info using Plugin Name as key
    print("Creating plugin lookup dictionary...")
    plugin_lookup = {}
    for item in plugin_info_data:
        plugin_name = item.get("Plugin Name")
        if plugin_name:
            plugin_lookup[plugin_name] = item.get("more_info", "")

    print(f"Found {len(plugin_lookup)} plugins in lookup data")

    # Enrich the offline data
    print("Enriching offline data...")
    enriched_count = 0
    total_count = len(offline_data)

    for entry in offline_data:
        plugin_name = entry.get("Plugin Name")
        if plugin_name and plugin_name in plugin_lookup:
            # Add more_info field after Remediation Steps
            more_info = plugin_lookup[plugin_name]
            if more_info:  # Only add if more_info is not empty
                entry["more_info"] = more_info
                enriched_count += 1
        elif plugin_name:
            # Plugin not found, add empty more_info
            entry["more_info"] = ""

    print(f"Enriched {enriched_count} out of {total_count} entries")

    # Save the enriched data
    print(f"Saving enriched data to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(offline_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Successfully enriched Azure offline data!")
    print(f"📄 Output file: {output_path}")
    print(f"📊 Total entries: {total_count}")
    print(f"✨ Enriched entries: {enriched_count}")

    # Show some statistics
    plugins_found = set()
    plugins_not_found = set()

    for entry in offline_data:
        plugin_name = entry.get("Plugin Name")
        if plugin_name:
            if plugin_name in plugin_lookup:
                plugins_found.add(plugin_name)
            else:
                plugins_not_found.add(plugin_name)

    print(f"🔍 Unique plugins found: {len(plugins_found)}")
    print(f"❌ Unique plugins not found: {len(plugins_not_found)}")

    if plugins_not_found:
        print("\nPlugins not found in plugin_info_only.json:")
        for plugin in sorted(list(plugins_not_found))[:10]:  # Show first 10
            print(f"  - {plugin}")
        if len(plugins_not_found) > 10:
            print(f"  ... and {len(plugins_not_found) - 10} more")


if __name__ == "__main__":
    try:
        enrich_azure_data()
    except FileNotFoundError as e:
        print(f"❌ Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"❌ Error: {e}")
