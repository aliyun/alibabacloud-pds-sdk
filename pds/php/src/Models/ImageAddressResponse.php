<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\Address;

/**
 * *
 */
class ImageAddressResponse extends Model {
    protected $_name = [
        'addressDetail' => 'address_detail',
        'count' => 'count',
        'coverFileId' => 'cover_file_id',
        'coverUrl' => 'cover_url',
        'location' => 'location',
        'name' => 'name',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->addressDetail) {
            $res['address_detail'] = null !== $this->addressDetail ? $this->addressDetail->toMap() : null;
        }
        if (null !== $this->count) {
            $res['count'] = $this->count;
        }
        if (null !== $this->coverFileId) {
            $res['cover_file_id'] = $this->coverFileId;
        }
        if (null !== $this->coverUrl) {
            $res['cover_url'] = $this->coverUrl;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return ImageAddressResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['address_detail'])){
            $model->addressDetail = Address::fromMap($map['address_detail']);
        }
        if(isset($map['count'])){
            $model->count = $map['count'];
        }
        if(isset($map['cover_file_id'])){
            $model->coverFileId = $map['cover_file_id'];
        }
        if(isset($map['cover_url'])){
            $model->coverUrl = $map['cover_url'];
        }
        if(isset($map['location'])){
            $model->location = $map['location'];
        }
        if(isset($map['name'])){
            $model->name = $map['name'];
        }
        return $model;
    }
    /**
     * @var Address
     */
    public $addressDetail;

    /**
     * @description 聚类地点计数
     * @example 1
     * @var int
     */
    public $count;

    /**
     * @description cover_file_id
     * @var string
     */
    public $coverFileId;

    /**
     * @description 聚类地点封面图片地址
     * @example http://imm-dev-wmt/tags/05.jpg?x-oss-process=xxx
     * @var string
     */
    public $coverUrl;

    /**
     * @description 经纬度
     * @example 39.21211,101.32111
     * @var string
     */
    public $location;

    /**
     * @description 聚类地点名称
     * @example 杭州
     * @var string
     */
    public $name;

}
