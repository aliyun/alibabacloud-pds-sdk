// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageMediaResponse extends TeaModel {
    // address_line
    @NameInMap("address_line")
    public String addressLine;

    // city
    @NameInMap("city")
    public String city;

    // country
    @NameInMap("country")
    public String country;

    // cropping_suggestion
    @NameInMap("cropping_suggestion")
    public java.util.List<CroppingSuggestionItem> croppingSuggestion;

    // district
    @NameInMap("district")
    public String district;

    // exif json string
    @NameInMap("exif")
    public String exif;

    // faces json string
    @NameInMap("faces")
    public String faces;

    // height
    @NameInMap("height")
    public Long height;

    @NameInMap("image_quality")
    public ImageQuality imageQuality;

    // system_tags
    @NameInMap("image_tags")
    public java.util.List<SystemTag> imageTags;

    // location
    @NameInMap("location")
    public String location;

    // province
    @NameInMap("province")
    public String province;

    // story_image_score
    @NameInMap("story_image_score")
    public Double storyImageScore;

    // time
    @NameInMap("time")
    public String time;

    // township
    @NameInMap("township")
    public String township;

    // width
    @NameInMap("width")
    public Long width;

    public static ImageMediaResponse build(java.util.Map<String, ?> map) throws Exception {
        ImageMediaResponse self = new ImageMediaResponse();
        return TeaModel.build(map, self);
    }

    public ImageMediaResponse setAddressLine(String addressLine) {
        this.addressLine = addressLine;
        return this;
    }
    public String getAddressLine() {
        return this.addressLine;
    }

    public ImageMediaResponse setCity(String city) {
        this.city = city;
        return this;
    }
    public String getCity() {
        return this.city;
    }

    public ImageMediaResponse setCountry(String country) {
        this.country = country;
        return this;
    }
    public String getCountry() {
        return this.country;
    }

    public ImageMediaResponse setCroppingSuggestion(java.util.List<CroppingSuggestionItem> croppingSuggestion) {
        this.croppingSuggestion = croppingSuggestion;
        return this;
    }
    public java.util.List<CroppingSuggestionItem> getCroppingSuggestion() {
        return this.croppingSuggestion;
    }

    public ImageMediaResponse setDistrict(String district) {
        this.district = district;
        return this;
    }
    public String getDistrict() {
        return this.district;
    }

    public ImageMediaResponse setExif(String exif) {
        this.exif = exif;
        return this;
    }
    public String getExif() {
        return this.exif;
    }

    public ImageMediaResponse setFaces(String faces) {
        this.faces = faces;
        return this;
    }
    public String getFaces() {
        return this.faces;
    }

    public ImageMediaResponse setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public ImageMediaResponse setImageQuality(ImageQuality imageQuality) {
        this.imageQuality = imageQuality;
        return this;
    }
    public ImageQuality getImageQuality() {
        return this.imageQuality;
    }

    public ImageMediaResponse setImageTags(java.util.List<SystemTag> imageTags) {
        this.imageTags = imageTags;
        return this;
    }
    public java.util.List<SystemTag> getImageTags() {
        return this.imageTags;
    }

    public ImageMediaResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public ImageMediaResponse setProvince(String province) {
        this.province = province;
        return this;
    }
    public String getProvince() {
        return this.province;
    }

    public ImageMediaResponse setStoryImageScore(Double storyImageScore) {
        this.storyImageScore = storyImageScore;
        return this;
    }
    public Double getStoryImageScore() {
        return this.storyImageScore;
    }

    public ImageMediaResponse setTime(String time) {
        this.time = time;
        return this;
    }
    public String getTime() {
        return this.time;
    }

    public ImageMediaResponse setTownship(String township) {
        this.township = township;
        return this;
    }
    public String getTownship() {
        return this.township;
    }

    public ImageMediaResponse setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
