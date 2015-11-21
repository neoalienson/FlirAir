//
//  SecondViewController.swift
//  FlirAir
//
//  Created by Neo on 11/21/15.
//  Copyright © 2015 padblish. All rights reserved.
//

import UIKit

class ModeViewController: UIViewController {

    @IBOutlet weak var buttonAimed: UIButton!
    @IBOutlet weak var buttonEars: UIButton!
    @IBOutlet weak var buttonStrong: UIButton!
    
    func request(mode: String) {
        let url = NSURL(string: "http://flir.hopto.org:8000/" + mode)
        
        let task = NSURLSession.sharedSession().dataTaskWithURL(url!) {(data, response, error) in
            print("error")
        }
        
        task.resume()
    }
    
    @IBAction func buttonUp(sender: AnyObject) {
        let button = sender as! UIButton
        buttonAimed.setImage(UIImage(named: ((button == buttonAimed) ? "mode_aimed" : "mode_aimed_b")),
            forState: UIControlState.Normal)
        buttonEars.setImage(UIImage(named: (button == buttonEars) ? "mode_ears" : "mode_ears_b"),
            forState: UIControlState.Normal)
        buttonStrong.setImage(UIImage(named: (button == buttonStrong) ? "mode_strong" : "mode_strong_b"),
            forState: UIControlState.Normal)
        
        switch (button) {
        case buttonAimed:
            request("mode_aimed")
            break
        case buttonEars:
            request("mode_ears")
            break
        case buttonAimed:
            request("mode_strong")
            break
        default:
            break
            
        }
    }
    

    
}

