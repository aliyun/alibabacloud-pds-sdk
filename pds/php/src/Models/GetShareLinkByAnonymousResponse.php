<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get_share_link_by_anonymous response
 */
class GetShareLinkByAnonymousResponse extends Model {
    protected $_name = [
        'avatar' => 'avatar',
        'creatorId' => 'creator_id',
        'creatorName' => 'creator_name',
        'creatorPhone' => 'creator_phone',
        'expiration' => 'expiration',
        'shareName' => 'share_name',
        'updatedAt' => 'updated_at',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->avatar) {
            $res['avatar'] = $this->avatar;
        }
        if (null !== $this->creatorId) {
            $res['creator_id'] = $this->creatorId;
        }
        if (null !== $this->creatorName) {
            $res['creator_name'] = $this->creatorName;
        }
        if (null !== $this->creatorPhone) {
            $res['creator_phone'] = $this->creatorPhone;
        }
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->shareName) {
            $res['share_name'] = $this->shareName;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetShareLinkByAnonymousResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['avatar'])){
            $model->avatar = $map['avatar'];
        }
        if(isset($map['creator_id'])){
            $model->creatorId = $map['creator_id'];
        }
        if(isset($map['creator_name'])){
            $model->creatorName = $map['creator_name'];
        }
        if(isset($map['creator_phone'])){
            $model->creatorPhone = $map['creator_phone'];
        }
        if(isset($map['expiration'])){
            $model->expiration = $map['expiration'];
        }
        if(isset($map['share_name'])){
            $model->shareName = $map['share_name'];
        }
        if(isset($map['updated_at'])){
            $model->updatedAt = $map['updated_at'];
        }
        return $model;
    }
    /**
     * @description avatar
     * @example https://abcd.com/efgh
     * @var string
     */
    public $avatar;

    /**
     * @description creator_id
     * @example zhangsan
     * @var string
     */
    public $creatorId;

    /**
     * @description creator_name
     * @example ABC**FG
     * @var string
     */
    public $creatorName;

    /**
     * @description creator_phone
     * @example 180**32
     * @var string
     */
    public $creatorPhone;

    /**
     * @description expiration
     * @example 2019-08-20T06:51:27.292Z
     * @var string
     */
    public $expiration;

    /**
     * @description share_name
     * @example name
     * @var string
     */
    public $shareName;

    /**
     * @description updated_at
     * @var string
     */
    public $updatedAt;

}
