// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageQuality extends TeaModel {
    @NameInMap("clarity")
    public Integer clarity;

    @NameInMap("clarity_score")
    public Integer clarityScore;

    @NameInMap("color")
    public Integer color;

    @NameInMap("color_score")
    public Integer colorScore;

    @NameInMap("composition_score")
    public Integer compositionScore;

    @NameInMap("contrast")
    public Integer contrast;

    @NameInMap("contrast_score")
    public Integer contrastScore;

    @NameInMap("exposure")
    public Integer exposure;

    @NameInMap("exposure_score")
    public Integer exposureScore;

    @NameInMap("overall_score")
    public Integer overallScore;

    public static ImageQuality build(java.util.Map<String, ?> map) throws Exception {
        ImageQuality self = new ImageQuality();
        return TeaModel.build(map, self);
    }

    public ImageQuality setClarity(Integer clarity) {
        this.clarity = clarity;
        return this;
    }
    public Integer getClarity() {
        return this.clarity;
    }

    public ImageQuality setClarityScore(Integer clarityScore) {
        this.clarityScore = clarityScore;
        return this;
    }
    public Integer getClarityScore() {
        return this.clarityScore;
    }

    public ImageQuality setColor(Integer color) {
        this.color = color;
        return this;
    }
    public Integer getColor() {
        return this.color;
    }

    public ImageQuality setColorScore(Integer colorScore) {
        this.colorScore = colorScore;
        return this;
    }
    public Integer getColorScore() {
        return this.colorScore;
    }

    public ImageQuality setCompositionScore(Integer compositionScore) {
        this.compositionScore = compositionScore;
        return this;
    }
    public Integer getCompositionScore() {
        return this.compositionScore;
    }

    public ImageQuality setContrast(Integer contrast) {
        this.contrast = contrast;
        return this;
    }
    public Integer getContrast() {
        return this.contrast;
    }

    public ImageQuality setContrastScore(Integer contrastScore) {
        this.contrastScore = contrastScore;
        return this;
    }
    public Integer getContrastScore() {
        return this.contrastScore;
    }

    public ImageQuality setExposure(Integer exposure) {
        this.exposure = exposure;
        return this;
    }
    public Integer getExposure() {
        return this.exposure;
    }

    public ImageQuality setExposureScore(Integer exposureScore) {
        this.exposureScore = exposureScore;
        return this;
    }
    public Integer getExposureScore() {
        return this.exposureScore;
    }

    public ImageQuality setOverallScore(Integer overallScore) {
        this.overallScore = overallScore;
        return this;
    }
    public Integer getOverallScore() {
        return this.overallScore;
    }

}
