// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageMediaResponse extends TeaModel {
    /**
     * <p>address_line</p>
     */
    @NameInMap("address_line")
    public String addressLine;

    /**
     * <p>city</p>
     */
    @NameInMap("city")
    public String city;

    /**
     * <p>country</p>
     */
    @NameInMap("country")
    public String country;

    /**
     * <p>cropping_suggestion</p>
     */
    @NameInMap("cropping_suggestion")
    public java.util.List<CroppingSuggestionItem> croppingSuggestion;

    /**
     * <p>district</p>
     */
    @NameInMap("district")
    public String district;

    /**
     * <p>exif json string</p>
     */
    @NameInMap("exif")
    public String exif;

    /**
     * <p>faces json string</p>
     */
    @NameInMap("faces")
    public String faces;

    /**
     * <p>faces_thumbnail_list</p>
     */
    @NameInMap("faces_thumbnail")
    public java.util.List<FaceThumbnail> facesThumbnail;

    /**
     * <p>height</p>
     */
    @NameInMap("height")
    public Long height;

    @NameInMap("image_quality")
    public ImageQuality imageQuality;

    /**
     * <p>system_tags</p>
     */
    @NameInMap("image_tags")
    public java.util.List<SystemTag> imageTags;

    /**
     * <p>location</p>
     */
    @NameInMap("location")
    public String location;

    /**
     * <p>province</p>
     */
    @NameInMap("province")
    public String province;

    /**
     * <p>time</p>
     */
    @NameInMap("time")
    public String time;

    /**
     * <p>township</p>
     */
    @NameInMap("township")
    public String township;

    /**
     * <p>width</p>
     */
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

    public ImageMediaResponse setFacesThumbnail(java.util.List<FaceThumbnail> facesThumbnail) {
        this.facesThumbnail = facesThumbnail;
        return this;
    }
    public java.util.List<FaceThumbnail> getFacesThumbnail() {
        return this.facesThumbnail;
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
