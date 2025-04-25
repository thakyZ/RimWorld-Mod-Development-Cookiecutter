using System;
using UnityEngine;
using Verse;
using RimWorld;
using HarmonyLib;
namespace {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }};
  public static {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings Settings { get; private set; }

  internal static Harmony Harmony { get; private set; }

    public override string SettingsCategory() => "{{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}.Settings.Title".Translate();
}

public class {{ cookiecutter.mod_name.replace('-','_').replace(' ','') }}Settings : ModSettings
{
    public bool debugLog = false;
    public override void ExposeData()
    {
        Scribe_Values.Look(ref debugLog, "debugLog", false);
        base.ExposeData();
    }
}
