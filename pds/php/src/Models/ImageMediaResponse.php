<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ImageMediaResponse extends Model
{
    /**
     * @description address_line
     *
     * @example 北京市昌平区白各庄新村路
     *
     * @var string
     */
    public $addressLine;

    /**
     * @description city
     *
     * @example 杭州
     *
     * @var string
     */
    public $city;

    /**
     * @description country
     *
     * @example 中国
     *
     * @var string
     */
    public $country;

    /**
     * @description cropping_suggestion
     *
     * @var CroppingSuggestionItem[]
     */
    public $croppingSuggestion;

    /**
     * @description district
     *
     * @example 余杭区
     *
     * @var string
     */
    public $district;

    /**
     * @description exif json string
     *
     * @var string
     */
    public $exif;

    /**
     * @description faces json string
     *
     * @var string
     */
    public $faces;

    /**
     * @description height
     *
     * @example 720
     *
     * @var int
     */
    public $height;

    /**
     * @var ImageQuality
     */
    public $imageQuality;

    /**
     * @description system_tags
     *
     * @var SystemTag[]
     */
    public $imageTags;

    /**
     * @description location
     *
     * @example 40.110333,116.349311
     *
     * @var string
     */
    public $location;

    /**
     * @description province
     *
     * @example 浙江省
     *
     * @var string
     */
    public $province;

    /**
     * @description story_image_score
     *
     * @var float
     */
    public $storyImageScore;

    /**
     * @description time
     *
     * @var string
     */
    public $time;

    /**
     * @description township
     *
     * @example 沙河镇
     *
     * @var string
     */
    public $township;

    /**
     * @description width
     *
     * @example 1024
     *
     * @var int
     */
    public $width;
    protected $_name = [
        'addressLine'        => 'address_line',
        'city'               => 'city',
        'country'            => 'country',
        'croppingSuggestion' => 'cropping_suggestion',
        'district'           => 'district',
        'exif'               => 'exif',
        'faces'              => 'faces',
        'height'             => 'height',
        'imageQuality'       => 'image_quality',
        'imageTags'          => 'image_tags',
        'location'           => 'location',
        'province'           => 'province',
        'storyImageScore'    => 'story_image_score',
        'time'               => 'time',
        'township'           => 'township',
        'width'              => 'width',
    ];
    protected $_default = [
        'height' => 0,
        'width'  => 0,
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->addressLine) {
            $res['address_line'] = $this->addressLine;
        }
        if (null !== $this->city) {
            $res['city'] = $this->city;
        }
        if (null !== $this->country) {
            $res['country'] = $this->country;
        }
        if (null !== $this->croppingSuggestion) {
            $res['cropping_suggestion'] = [];
            if (null !== $this->croppingSuggestion && \is_array($this->croppingSuggestion)) {
                $n = 0;
                foreach ($this->croppingSuggestion as $item) {
                    $res['cropping_suggestion'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->district) {
            $res['district'] = $this->district;
        }
        if (null !== $this->exif) {
            $res['exif'] = $this->exif;
        }
        if (null !== $this->faces) {
            $res['faces'] = $this->faces;
        }
        if (null !== $this->height) {
            $res['height'] = $this->height;
        }
        if (null !== $this->imageQuality) {
            $res['image_quality'] = null !== $this->imageQuality ? $this->imageQuality->toMap() : null;
        }
        if (null !== $this->imageTags) {
            $res['image_tags'] = [];
            if (null !== $this->imageTags && \is_array($this->imageTags)) {
                $n = 0;
                foreach ($this->imageTags as $item) {
                    $res['image_tags'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->province) {
            $res['province'] = $this->province;
        }
        if (null !== $this->storyImageScore) {
            $res['story_image_score'] = $this->storyImageScore;
        }
        if (null !== $this->time) {
            $res['time'] = $this->time;
        }
        if (null !== $this->township) {
            $res['township'] = $this->township;
        }
        if (null !== $this->width) {
            $res['width'] = $this->width;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ImageMediaResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['address_line'])) {
            $model->addressLine = $map['address_line'];
        }
        if (isset($map['city'])) {
            $model->city = $map['city'];
        }
        if (isset($map['country'])) {
            $model->country = $map['country'];
        }
        if (isset($map['cropping_suggestion'])) {
            if (!empty($map['cropping_suggestion'])) {
                $model->croppingSuggestion = [];
                $n                         = 0;
                foreach ($map['cropping_suggestion'] as $item) {
                    $model->croppingSuggestion[$n++] = null !== $item ? CroppingSuggestionItem::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['district'])) {
            $model->district = $map['district'];
        }
        if (isset($map['exif'])) {
            $model->exif = $map['exif'];
        }
        if (isset($map['faces'])) {
            $model->faces = $map['faces'];
        }
        if (isset($map['height'])) {
            $model->height = $map['height'];
        }
        if (isset($map['image_quality'])) {
            $model->imageQuality = ImageQuality::fromMap($map['image_quality']);
        }
        if (isset($map['image_tags'])) {
            if (!empty($map['image_tags'])) {
                $model->imageTags = [];
                $n                = 0;
                foreach ($map['image_tags'] as $item) {
                    $model->imageTags[$n++] = null !== $item ? SystemTag::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['location'])) {
            $model->location = $map['location'];
        }
        if (isset($map['province'])) {
            $model->province = $map['province'];
        }
        if (isset($map['story_image_score'])) {
            $model->storyImageScore = $map['story_image_score'];
        }
        if (isset($map['time'])) {
            $model->time = $map['time'];
        }
        if (isset($map['township'])) {
            $model->township = $map['township'];
        }
        if (isset($map['width'])) {
            $model->width = $map['width'];
        }

        return $model;
    }
}
