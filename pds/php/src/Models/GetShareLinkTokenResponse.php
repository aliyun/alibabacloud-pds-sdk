<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get_share_token response.
 */
class GetShareLinkTokenResponse extends Model
{
    /**
     * @description expire_time
     *
     * @example 2019-09-01T06:57:48.813Z
     *
     * @var string
     */
    public $expireTime;

    /**
     * @description expires_in
     *
     * @example 3600
     *
     * @var int
     */
    public $expiresIn;

    /**
     * @description share_token
     *
     * @example cnskjajkahwdhwialsnd
     *
     * @var string
     */
    public $shareToken;
    protected $_name = [
        'expireTime' => 'expire_time',
        'expiresIn'  => 'expires_in',
        'shareToken' => 'share_token',
    ];

    public function validate()
    {
        Model::validateRequired('expireTime', $this->expireTime, true);
        Model::validateRequired('expiresIn', $this->expiresIn, true);
        Model::validateRequired('shareToken', $this->shareToken, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->expireTime) {
            $res['expire_time'] = $this->expireTime;
        }
        if (null !== $this->expiresIn) {
            $res['expires_in'] = $this->expiresIn;
        }
        if (null !== $this->shareToken) {
            $res['share_token'] = $this->shareToken;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetShareLinkTokenResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['expire_time'])) {
            $model->expireTime = $map['expire_time'];
        }
        if (isset($map['expires_in'])) {
            $model->expiresIn = $map['expires_in'];
        }
        if (isset($map['share_token'])) {
            $model->shareToken = $map['share_token'];
        }

        return $model;
    }
}
