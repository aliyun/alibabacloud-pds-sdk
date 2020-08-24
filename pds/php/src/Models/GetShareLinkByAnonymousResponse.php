<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get_share_link_by_anonymous response.
 */
class GetShareLinkByAnonymousResponse extends Model
{
    /**
     * @description creator_id
     *
     * @example zhangsan
     *
     * @var string
     */
    public $creatorId;

    /**
     * @description creator_name
     *
     * @example ABC**FG
     *
     * @var string
     */
    public $creatorName;

    /**
     * @description expiration
     *
     * @example 2006-01-02T15:04:05.999Z07:00
     *
     * @var string
     */
    public $expiration;

    /**
     * @description updated_at
     *
     * @var string
     */
    public $updatedAt;
    protected $_name = [
        'creatorId'   => 'creator_id',
        'creatorName' => 'creator_name',
        'expiration'  => 'expiration',
        'updatedAt'   => 'updated_at',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->creatorId) {
            $res['creator_id'] = $this->creatorId;
        }
        if (null !== $this->creatorName) {
            $res['creator_name'] = $this->creatorName;
        }
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetShareLinkByAnonymousResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['creator_id'])) {
            $model->creatorId = $map['creator_id'];
        }
        if (isset($map['creator_name'])) {
            $model->creatorName = $map['creator_name'];
        }
        if (isset($map['expiration'])) {
            $model->expiration = $map['expiration'];
        }
        if (isset($map['updated_at'])) {
            $model->updatedAt = $map['updated_at'];
        }

        return $model;
    }
}
