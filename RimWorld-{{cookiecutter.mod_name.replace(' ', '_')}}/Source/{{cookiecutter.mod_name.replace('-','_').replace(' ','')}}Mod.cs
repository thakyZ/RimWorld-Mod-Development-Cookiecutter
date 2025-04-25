using System;
using UnityEngine;
using Verse;
using RimWorld;
using HarmonyLib;

namespace {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }};

/// <summary>
/// The entrypoint for this mod.
/// </summary>
public class {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Mod : Mod {
  /// <summary>
  /// Gets an instance of the mod's settings.
  /// </summary>
  public static {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings? Settings { get; private set; }

  /// <summary>
  /// Gets an instance of the mod's constructed <see cref="Harmony" /> patcher.
  /// </summary>
  internal static Harmony? Harmony { get; private set; }

  /// <summary>
  /// Initializes a new instance of the <see cref="{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Mod" /> class.",
  /// </summary>
  public {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Mod(ModContentPack content) : base(content) {
    Settings = GetSettings<{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings>();
    Harmony = new("{{ cookiecutter.package_id }}");
    Harmony.PatchAll();
  }

  /// <summary>
  /// Renders the contents of the settings window for this mod.
  /// </summary>
  /// <param name="inRect">A <see cref="Rect" /> that determines the bounds of the settings window.</param>
  public override void DoSettingsWindowContents(Rect inRect) {
    Listing_Standard listingStandard = new();
    listingStandard.Begin(inRect);
    Widgets.CheckboxLabeled(inRect, "{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}.Settings.Debug".TranslateSimple(), ref Settings.debugLog);
    // Your code here...
    listingStandard.End();
    base.DoSettingsWindowContents(inRect);
  }

  /// <summary>
  /// Gets the title <see langword="string" /> of settings window.
  /// </summary>
  /// <returns>A <see langword="string" /> representing the title of the settings window.</returns>
  public override string SettingsCategory() => "{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}.Settings.Title".Translate();
}

/// <summary>
/// A class to specify the settings of the <see cref="{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Mod" /> class.
/// </summary>
public class {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings : ModSettings {
  /// <summary>
  /// A <see langword="bool" /> that determines if the mod should debug log.
  /// </summary>
  public bool debugLog = false;

  /// <summary>
  /// Exposes the data to the config file of this mod.
  /// </summary>
  public override void ExposeData() {
    Scribe_Values.Look(ref debugLog, "debugLog", false);
    base.ExposeData();
  }
}
