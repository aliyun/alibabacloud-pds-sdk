<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class TokenRequest extends Model
{
    /**
     * @description JWT方式授权需要传此参数，传入JWT签名的声明，用于更换accessToken
     *
     * @example ak******asd==
     *
     * @var string
     */
    public $Assertion;

    /**
     * @description Client ID, 此处填写创建App时返回的AppID
     *
     * @example aksjoiajsoias
     *
     * @var string
     */
    public $ClientID;

    /**
     * @description Client ID, 此处填写创建App时返回的AppSecret
     *
     * @example alsdklajdkxlawalwknq
     *
     * @var string
     */
    public $ClientSecret;

    /**
     * @description 认证后回调参数中的code
     *
     * @example cjajksadhw
     *
     * @var string
     */
    public $Code;

    /**
     * @description OAuth2.0 device flow换取token参数
     *
     * @example cjajksadhw
     *
     * @var string
     */
    public $DeviceCode;

    /**
     * @description 通过code获取accessToken或者通过refresh_token获取accessToken
     *
     * @example authorization_code
     *
     * @var string
     */
    public $GrantType;

    /**
     * @description 回调地址, 此处填写创建App时填写的回调地址，OAuth方式登录时需要传入
     *
     * @example https://app.com/callback
     *
     * @var string
     */
    public $RedirectUri;

    /**
     * @description 刷新accessToken使用的refreshToken
     *
     * @example aksbcjhwhq
     *
     * @var string
     */
    public $RefreshToken;

    /**
     * @description SubDomainID
     *
     * @example null
     *
     * @var string
     */
    public $SubDomainID;
    protected $_name = [
        'Assertion'    => 'Assertion',
        'ClientID'     => 'ClientID',
        'ClientSecret' => 'ClientSecret',
        'Code'         => 'Code',
        'DeviceCode'   => 'DeviceCode',
        'GrantType'    => 'GrantType',
        'RedirectUri'  => 'RedirectUri',
        'RefreshToken' => 'RefreshToken',
        'SubDomainID'  => 'SubDomainID',
    ];

    public function validate()
    {
        Model::validateRequired('ClientID', $this->ClientID, true);
        Model::validateRequired('ClientSecret', $this->ClientSecret, true);
        Model::validateRequired('GrantType', $this->GrantType, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->Assertion) {
            $res['Assertion'] = $this->Assertion;
        }
        if (null !== $this->ClientID) {
            $res['ClientID'] = $this->ClientID;
        }
        if (null !== $this->ClientSecret) {
            $res['ClientSecret'] = $this->ClientSecret;
        }
        if (null !== $this->Code) {
            $res['Code'] = $this->Code;
        }
        if (null !== $this->DeviceCode) {
            $res['DeviceCode'] = $this->DeviceCode;
        }
        if (null !== $this->GrantType) {
            $res['GrantType'] = $this->GrantType;
        }
        if (null !== $this->RedirectUri) {
            $res['RedirectUri'] = $this->RedirectUri;
        }
        if (null !== $this->RefreshToken) {
            $res['RefreshToken'] = $this->RefreshToken;
        }
        if (null !== $this->SubDomainID) {
            $res['SubDomainID'] = $this->SubDomainID;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return TokenRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['Assertion'])) {
            $model->Assertion = $map['Assertion'];
        }
        if (isset($map['ClientID'])) {
            $model->ClientID = $map['ClientID'];
        }
        if (isset($map['ClientSecret'])) {
            $model->ClientSecret = $map['ClientSecret'];
        }
        if (isset($map['Code'])) {
            $model->Code = $map['Code'];
        }
        if (isset($map['DeviceCode'])) {
            $model->DeviceCode = $map['DeviceCode'];
        }
        if (isset($map['GrantType'])) {
            $model->GrantType = $map['GrantType'];
        }
        if (isset($map['RedirectUri'])) {
            $model->RedirectUri = $map['RedirectUri'];
        }
        if (isset($map['RefreshToken'])) {
            $model->RefreshToken = $map['RefreshToken'];
        }
        if (isset($map['SubDomainID'])) {
            $model->SubDomainID = $map['SubDomainID'];
        }

        return $model;
    }
}
