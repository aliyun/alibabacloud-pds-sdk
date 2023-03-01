// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseMediaResponse extends TeaModel {
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
     * <p>district</p>
     */
    @NameInMap("district")
    public String district;

    /**
     * <p>height</p>
     */
    @NameInMap("height")
    public Long height;

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

    public static BaseMediaResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseMediaResponse self = new BaseMediaResponse();
        return TeaModel.build(map, self);
    }

    public BaseMediaResponse setAddressLine(String addressLine) {
        this.addressLine = addressLine;
        return this;
    }
    public String getAddressLine() {
        return this.addressLine;
    }

    public BaseMediaResponse setCity(String city) {
        this.city = city;
        return this;
    }
    public String getCity() {
        return this.city;
    }

    public BaseMediaResponse setCountry(String country) {
        this.country = country;
        return this;
    }
    public String getCountry() {
        return this.country;
    }

    public BaseMediaResponse setDistrict(String district) {
        this.district = district;
        return this;
    }
    public String getDistrict() {
        return this.district;
    }

    public BaseMediaResponse setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public BaseMediaResponse setImageTags(java.util.List<SystemTag> imageTags) {
        this.imageTags = imageTags;
        return this;
    }
    public java.util.List<SystemTag> getImageTags() {
        return this.imageTags;
    }

    public BaseMediaResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public BaseMediaResponse setProvince(String province) {
        this.province = province;
        return this;
    }
    public String getProvince() {
        return this.province;
    }

    public BaseMediaResponse setTime(String time) {
        this.time = time;
        return this;
    }
    public String getTime() {
        return this.time;
    }

    public BaseMediaResponse setTownship(String township) {
        this.township = township;
        return this;
    }
    public String getTownship() {
        return this.township;
    }

    public BaseMediaResponse setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
