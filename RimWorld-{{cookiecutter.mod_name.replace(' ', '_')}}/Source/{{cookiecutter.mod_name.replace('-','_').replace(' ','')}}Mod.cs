using System;
using UnityEngine;
using Verse;
using RimWorld;
using HarmonyLib;
namespace {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }};
public class {{ cookiecutter.mod_nam.replace('-','_').replace(' ','') }}Mod : Mod
{
    public static readonly {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings settings;
    private static readonly Harmony harmony;
    public {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Mod(ModContentPack content) : base(content)
    {
        settings = GetSettings<{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings>();
        harmony = new("{{ cookiecutter.package_id }}");
        harmony.PatchAll();
    }

    public override void DoSettingsWindowContents(Rect inRect)
    {
        Listing_Standard listingStandard = new();
        listingStandard.Begin(inRect);
        Widgets.CheckboxLabeled(inRect, "{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}.Settings.Debug".TranslateSimple(), ref settings.debugLog);
        // Your code here...
        listingStandard.End();
        base.DoSettingsWindowContents(inRect);
    }

    public override string SettingsCategory() => "{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}.Settings.Title".Translate();
}

public class {{ cookiecutter.mod_nam.replace('-','_').replace(' ','') }}Settings : ModSettings
{
    public bool debugLog = false;
    public override void ExposeData()
    {
        Scribe_Values.Look(ref debugLog, "debugLog", false);
        base.ExposeData();
    }
}
