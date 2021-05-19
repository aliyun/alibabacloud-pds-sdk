// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageQuality extends TeaModel {
    @NameInMap("clarity")
    public Double clarity;

    @NameInMap("clarity_score")
    public Double clarityScore;

    @NameInMap("color")
    public Double color;

    @NameInMap("color_score")
    public Double colorScore;

    @NameInMap("composition_score")
    public Double compositionScore;

    @NameInMap("contrast")
    public Double contrast;

    @NameInMap("contrast_score")
    public Double contrastScore;

    @NameInMap("exposure")
    public Double exposure;

    @NameInMap("exposure_score")
    public Double exposureScore;

    @NameInMap("overall_score")
    public Double overallScore;

    public static ImageQuality build(java.util.Map<String, ?> map) throws Exception {
        ImageQuality self = new ImageQuality();
        return TeaModel.build(map, self);
    }

    public ImageQuality setClarity(Double clarity) {
        this.clarity = clarity;
        return this;
    }
    public Double getClarity() {
        return this.clarity;
    }

    public ImageQuality setClarityScore(Double clarityScore) {
        this.clarityScore = clarityScore;
        return this;
    }
    public Double getClarityScore() {
        return this.clarityScore;
    }

    public ImageQuality setColor(Double color) {
        this.color = color;
        return this;
    }
    public Double getColor() {
        return this.color;
    }

    public ImageQuality setColorScore(Double colorScore) {
        this.colorScore = colorScore;
        return this;
    }
    public Double getColorScore() {
        return this.colorScore;
    }

    public ImageQuality setCompositionScore(Double compositionScore) {
        this.compositionScore = compositionScore;
        return this;
    }
    public Double getCompositionScore() {
        return this.compositionScore;
    }

    public ImageQuality setContrast(Double contrast) {
        this.contrast = contrast;
        return this;
    }
    public Double getContrast() {
        return this.contrast;
    }

    public ImageQuality setContrastScore(Double contrastScore) {
        this.contrastScore = contrastScore;
        return this;
    }
    public Double getContrastScore() {
        return this.contrastScore;
    }

    public ImageQuality setExposure(Double exposure) {
        this.exposure = exposure;
        return this;
    }
    public Double getExposure() {
        return this.exposure;
    }

    public ImageQuality setExposureScore(Double exposureScore) {
        this.exposureScore = exposureScore;
        return this;
    }
    public Double getExposureScore() {
        return this.exposureScore;
    }

    public ImageQuality setOverallScore(Double overallScore) {
        this.overallScore = overallScore;
        return this;
    }
    public Double getOverallScore() {
        return this.overallScore;
    }

}
