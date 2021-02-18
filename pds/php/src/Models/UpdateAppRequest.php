<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class UpdateAppRequest extends Model
{
    /**
     * @description App ID
     *
     * @example CNMrhxwPJHAReExa
     *
     * @var string
     */
    public $appId;

    /**
     * @description App名称
     *
     * @example 图片分享应用
     *
     * @var string
     */
    public $appName;

    /**
     * @description App描述
     *
     * @example 测试专用
     *
     * @var string
     */
    public $description;

    /**
     * @description App图标
     *
     * @example https://app.com/logo.jpg
     *
     * @var string
     */
    public $logo;

    /**
     * @description App回调地址
     *
     * @example https://app.com/callback
     *
     * @var string
     */
    public $redirectUri;

    /**
     * @description App权限列表
     *
     * @var string[]
     */
    public $scope;

    /**
     * @description App类型
     *
     * @example WebServer
     *
     * @var string
     */
    public $type;
    protected $_name = [
        'appId'       => 'app_id',
        'appName'     => 'app_name',
        'description' => 'description',
        'logo'        => 'logo',
        'redirectUri' => 'redirect_uri',
        'scope'       => 'scope',
        'type'        => 'type',
    ];
    protected $_default = [
        'type' => 'WebServer',
    ];

    public function validate()
    {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateMaxLength('appName', $this->appName, 128);
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateMinLength('appName', $this->appName, 1);
        Model::validateMinLength('description', $this->description, 0);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->appName) {
            $res['app_name'] = $this->appName;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->logo) {
            $res['logo'] = $this->logo;
        }
        if (null !== $this->redirectUri) {
            $res['redirect_uri'] = $this->redirectUri;
        }
        if (null !== $this->scope) {
            $res['scope'] = $this->scope;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return UpdateAppRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['app_id'])) {
            $model->appId = $map['app_id'];
        }
        if (isset($map['app_name'])) {
            $model->appName = $map['app_name'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['logo'])) {
            $model->logo = $map['logo'];
        }
        if (isset($map['redirect_uri'])) {
            $model->redirectUri = $map['redirect_uri'];
        }
        if (isset($map['scope'])) {
            if (!empty($map['scope'])) {
                $model->scope = $map['scope'];
            }
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }

        return $model;
    }
}
