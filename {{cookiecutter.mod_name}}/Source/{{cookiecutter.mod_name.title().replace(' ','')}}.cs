using System;
using UnityEngine;
using Verse;
using RimWorld;
using HarmonyLib;

namespace {{ cookiecutter.mod_name.title().replace(' ','') }};
public class {{ cookiecutter.mod_name.title().replace(' ','') }} : Mod
{
    public static readonly {{ cookiecutter.mod_name.title().replace(' ','') }}Settings settings;
    private static readonly Harmony harmony;
    public {{ cookiecutter.mod_name.title().replace(' ','') }}(ModContentPack content) : base(content)
    {
        settings = GetSettings<{{ cookiecutter.mod_name.title().replace(' ','') }}Settings>();
        harmony = new("{{ cookiecutter.mod_package_id }}");
        harmony.PatchAll();
    }

    public override void DoSettingsWindowContents(Rect inRect)
    {
        Listing_Standard listingStandard = new();
        listingStandard.Begin(inRect);
        // Your code here...
        listingStandard.End();
        base.DoSettingsWindowContents(inRect);
    }

    public override string SettingsCategory() => "{{ cookiecutter.mod_name.title().replace(' ','') }}.Settings.Title".Translate();
}

public class {{ cookiecutter.mod_name.title().replace(' ','') }}Settings : ModSettings
{
    public bool debugLog = false;
    public override void ExposeData()
    {
        Scribe_Values.Look(ref debugLog, "debugLog", false);
        base.ExposeData();
    }
}